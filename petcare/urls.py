from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (
    index_view,
    TutorViewSet, MascotaViewSet, VeterinarioViewSet,
    CitaMedicaViewSet, FichaMedicaViewSet, RecordatorioPreventivoViewSet
)

router = SimpleRouter()
router.register(r'tutores', TutorViewSet)
router.register(r'mascotas', MascotaViewSet)
router.register(r'veterinarios', VeterinarioViewSet)
router.register(r'citas', CitaMedicaViewSet)
router.register(r'fichas', FichaMedicaViewSet)
router.register(r'recordatorios', RecordatorioPreventivoViewSet)

urlpatterns = [
    path('', index_view, name='home'), 
    path('', include(router.urls)),
]