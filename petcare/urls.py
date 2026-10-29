from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tutores', views.TutorViewSet)
router.register(r'mascotas', views.MascotaViewSet)
router.register(r'veterinarios', views.VeterinarioViewSet)
router.register(r'citas', views.CitaMedicaViewSet)
router.register(r'fichas', views.FichaMedicaViewSet)
router.register(r'recordatorios', views.RecordatorioPreventivoViewSet)

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', include(router.urls)),
]