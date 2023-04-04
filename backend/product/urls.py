from django.urls import path, include
from rest_framework import routers

from product.views import ProductViewSet

router = routers.SimpleRouter()
router.register("product", ProductViewSet, basename="product")

app_name = "product"
urlpatterns = [path("", include(router.urls))]
