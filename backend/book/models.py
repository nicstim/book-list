from django.db import models

from book.utils.validators import validate_max_price


class Profile(models.Model):
    column_name = models.CharField("Название столбца", max_length=255)
    is_visible = models.BooleanField("Флаг видимости столбца", default=True)

    class Meta:
        verbose_name = "Настройка столбцов"
        verbose_name_plural = "Настройки столбцов"

    def __str__(self):
        return self.column_name


class Book(models.Model):
    name = models.CharField("Название", max_length=20)
    title = models.CharField("Заголовок", max_length=30, blank=True, null=True)
    author = models.CharField("Автор", max_length=30)
    description = models.CharField("Описание", max_length=512, blank=True, null=True)
    price = models.IntegerField("Цена", validators=[validate_max_price])

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.name
