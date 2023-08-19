"""Модуль содержит модели Настроек сайта."""
from typing import Any

from django.core.cache import cache
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.timezone import now


class SingletonModel(models.Model):
    """Модель-синглтон."""

    objects = models.Manager()

    class Meta:
        abstract = True

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()

    @classmethod
    def load(cls) -> object:
        """Метод возвращает экземпляр модели из кеша или создает его."""
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)

    def set_cache(self) -> None:
        """Метод устанавливает кеш экземпляр модели."""
        cache.set(self.__class__.__name__, self)


class SiteSettings(SingletonModel):
    """Модель Настроек сайта."""

    url = models.URLField(
        verbose_name="Website url",
        max_length=256)
    title = models.CharField(
        verbose_name="название сайта",
        max_length=256,
        default="Oil Mill"
    )
    email = models.EmailField(
        default="OILMILL@EMAIL.COM",
        verbose_name="электронная почта"
    )
    phone = models.CharField(
        max_length=256,
        verbose_name="телефон",
        default="+7 (7172) 77 77 77"
    )
    address = models.CharField(
        max_length=256,
        verbose_name="адрес",
        default="Г. АСТАНА, УЛ. ПРОМЫШЛЕННАЯ, ЗД.1",
    )
    telegram = models.CharField(
        max_length=256,
        verbose_name="telegram",
        default="@oil_mill"
    )
    whatsapp = models.CharField(
        max_length=256,
        verbose_name="whatsapp",
        default="whatsapp://send?phone=77172777777"
    )
    viber = models.CharField(
        max_length=256,
        verbose_name="viber",
        default="viber://chat?number=77172777777"
    )
    vk = models.CharField(
        max_length=256,
        verbose_name="vk",
        default=" https://vk.com/oilmill"
    )
    skype = models.CharField(
        max_length=256,
        verbose_name="skype",
        default="techno"
    )
    facebook = models.CharField(
        max_length=256,
        verbose_name="facebook",
        default="https://facebook.com/megano",
    )
    twitter = models.CharField(
        max_length=256,
        verbose_name="twitter",
        default="https://twitter.com/megano",
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата создания"
    )
    updated = models.DateTimeField(
        auto_now_add=True,
        verbose_name="дата обновления"
    )

    class Meta:
        db_table = "settings"
        verbose_name_plural = "Настройки"

    def __str__(self) -> str:
        """Метод для отображения информации об объекте класса SiteSettings."""
        return "Настройки"

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.updated = now()
        super().save(*args, **kwargs)
