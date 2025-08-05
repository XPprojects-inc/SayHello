# SayHello

This repository contains a simple utility to troubleshoot Roblox error 279, which prevents the client from connecting to game servers. The issue has been reported recently by players in Kazakhstan and Russia.

## Usage

1. Install dependencies:
   ```bash
   pip install requests
   ```
2. Run the helper script:
   ```bash
   python fix_error_279.py
   ```
3. Follow the on-screen instructions. The tool checks connectivity to Roblox, attempts to flush the DNS cache, and provides guidance for opening firewall ports required by Roblox.

The script cannot guarantee a full fix but automates common recovery steps and offers suggestions such as restarting the router or using a VPN if connectivity issues persist.

