from django.db import models


class Option(models.Model):
    title = models.CharField(max_length=255, help_text="Тип опций")
    price = models.DecimalField(decimal_places=2, max_digits=10, help_text="Цена")
    image = models.TextField(help_text="Ссылка на изображение")

    def __str__(self):
        return self.title
