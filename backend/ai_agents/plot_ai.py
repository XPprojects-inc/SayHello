"""Модуль первого ИИ, отвечающего за построение сюжета."""

from typing import List


def generate_plot(history: List[str]) -> str:
    """Возвращает черновой сюжет на основе истории просмотра.

    Параметры:
        history: список строк с описанием просмотренных видео.
    """
    if not history:
        return "Новый оригинальный сюжет без учёта истории."
    joined = ", ".join(history)
    return f"Сюжет, основанный на истории: {joined}."
