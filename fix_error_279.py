#!/usr/bin/env python3
"""Utility to troubleshoot and mitigate Roblox error 279.

Error 279 indicates the client cannot connect to the Roblox game servers.
This script performs a simple network check and attempts to flush DNS
and open the firewall for the ports Roblox uses on supported systems.
It does not guarantee a fix but can automate common recovery steps.
"""

import platform
import subprocess
import sys
from typing import List

try:
    import requests
except ImportError:  # pragma: no cover - dependency check
    requests = None

ROBLOX_URL = "https://www.roblox.com"


def check_connection() -> bool:
    """Return True if Roblox's website is reachable."""
    if requests is None:
        print("The requests library is not installed. Unable to test connectivity.")
        return False
    try:
        requests.get(ROBLOX_URL, timeout=5)
        print("Roblox website is reachable.")
        return True
    except Exception as exc:  # pragma: no cover - network dependent
        print("Unable to connect to Roblox:", exc)
        return False


def run_command(cmd: List[str]) -> None:
    """Run a command and handle errors gracefully."""
    print("Running:", " ".join(cmd))
    try:
        subprocess.run(cmd, check=True)
        print("Command completed successfully.")
    except Exception as exc:  # pragma: no cover - system dependent
        print("Command failed:", exc)
        print("Try running the command manually with administrator privileges.")


def flush_dns() -> None:
    """Attempt to flush the DNS cache on the current platform."""
    system = platform.system()
    if system == "Windows":
        run_command(["ipconfig", "/flushdns"])
    elif system == "Darwin":
        run_command(["dscacheutil", "-flushcache"])
    elif system == "Linux":
        run_command(["systemd-resolve", "--flush-caches"])
    else:
        print("Unsupported operating system for DNS flushing:", system)


def open_firewall_ports() -> None:
    """Attempt to open Roblox's recommended port range."""
    system = platform.system()
    if system == "Windows":
        tcp_cmd = [
            "netsh",
            "advfirewall",
            "firewall",
            "add",
            "rule",
            "name=RobloxTCP",
            "dir=in",
            "action=allow",
            "protocol=TCP",
            "localport=49152-65535",
        ]
        udp_cmd = [
            "netsh",
            "advfirewall",
            "firewall",
            "add",
            "rule",
            "name=RobloxUDP",
            "dir=in",
            "action=allow",
            "protocol=UDP",
            "localport=49152-65535",
        ]
        run_command(tcp_cmd)
        run_command(udp_cmd)
    elif system == "Linux":
        print(
            "Run these commands with administrator rights to open ports:\n"
            "  iptables -I INPUT -p tcp --dport 49152:65535 -j ACCEPT\n"
            "  iptables -I INPUT -p udp --dport 49152:65535 -j ACCEPT"
        )
    elif system == "Darwin":
        print(
            "Please open ports 49152-65535 in your firewall or router settings."
        )
    else:
        print("Unsupported operating system for firewall configuration:", system)


def main() -> None:
    print("Roblox Error 279 Troubleshooter")
    if check_connection():
        print("Connection to Roblox appears normal. If you still receive error 279,"
              " try restarting your router or using a VPN.")
        return
    print("Attempting to flush DNS cache...")
    flush_dns()
    print("Attempting to open firewall ports...")
    open_firewall_ports()
    print("Steps completed. Restart your computer and try Roblox again.")


if __name__ == "__main__":
    main()
