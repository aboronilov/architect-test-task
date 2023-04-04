from django.db import models
from base.models import Base
from material.models import Material
from option.models import Option
from size.models import Size


class Product(models.Model):
    image = models.TextField("Изображение товара")
    title = models.CharField(max_length=255, help_text="Наименование товара")
    slug = models.SlugField("Слаг товара")
    price = models.DecimalField(decimal_places=2, max_digits=10, help_text="Цена")
    # base = models.ForeignKey(Base, related_name="products", on_delete=models.CASCADE)
    # material = models.ForeignKey(
    #     Material, related_name="products", on_delete=models.CASCADE
    # )
    # option = models.ForeignKey(
    #     Option, related_name="products", on_delete=models.CASCADE
    # )
    # size = models.ForeignKey(Size, related_name="products", on_delete=models.CASCADE)
