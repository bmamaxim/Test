from django.db import models


NULLABLE = {"blank": True, "null": True}


class Factory(models.Model):
    """
    Класс модели Завод.
    """

    name = models.CharField(
        max_length=300,
        verbose_name="Название предприятия",
        help_text="Введите название предприятия",
        **NULLABLE,
    )
    email = models.EmailField(
        verbose_name="Электронная почта",
        help_text="Введите электронную почту",
        **NULLABLE,
    )
    country = models.CharField(
        max_length=150,
        verbose_name="Страна",
        help_text="Введите назваине страны",
        **NULLABLE,
    )
    city = models.CharField(
        max_length=150,
        verbose_name="Город",
        help_text="Введите название города",
        **NULLABLE,
    )
    street = models.CharField(
        max_length=150,
        verbose_name="Улица",
        help_text="Введите название улицы",
        **NULLABLE,
    )
    house = models.CharField(
        max_length=50,
        verbose_name="Номер дома",
        help_text="Введите номер дома",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.name} {self.email} {self.country} {self.city} {self.street} {self.house}"

    class Meta:
        verbose_name = "завод"
        verbose_name_plural = "заводы"


class Products(models.Model):
    """
    Класс продуктов предприятия.
    """

    manufacturer = models.ForeignKey(
        Factory,
        verbose_name="Производитель",
        help_text="Выберите производителя продукта",
        **NULLABLE,
    )
    name = models.CharField(
        max_length=150,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
        **NULLABLE,
    )
    model = models.CharField(
        max_length=200,
        verbose_name="Модель продукта",
        help_text="Введите модель продукта",
        **NULLABLE,
    )
    release = models.DateField(
        verbose_name="Дата выпуска",
        help_text="Назначте дату выпуска продукта",
        **NULLABLE,
    )
    date = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации", **NULLABLE
    )

    def __str__(self):
        return (
            f"{self.manufacturer} {self.name} {self.model} {self.release} {self.date}"
        )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
