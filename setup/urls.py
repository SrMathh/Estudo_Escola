
from django.contrib import admin
from django.urls import path,include
from escola.views import EstudanteViewSet,CursoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes',EstudanteViewSet)
router.register('cursos',CursoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]