from django.contrib import admin
from django.urls import path, include
from ecommerce.views import compradoresViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'compradores', compradoresViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
