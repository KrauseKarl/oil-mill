"""Модуль содержит контекст-процессоры настроек сайта."""
from typing import Dict

from django.http import HttpRequest

from .models import SiteSettings


def load_settings(request: HttpRequest) -> Dict[str, object]:
    """Функция возвращает астройки сайта."""
    return {"settings": SiteSettings.load()}
