from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from project.views import RegistroViewSet

router = routers.DefaultRouter()
router.register(r'registros', RegistroViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]