from django.db import models


class Size(models.Model):
    length = models.IntegerField(help_text="Длина")
    width = models.IntegerField(help_text="Ширина")
    percent_price = models.IntegerField(help_text="Прибавка к цене в %")

    def __str__(self):
        return f"{self.length} x {self.width}"
