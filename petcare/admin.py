from django.contrib import admin
from .models import Tutor, Mascota, Veterinario, CitaMedica, FichaMedica, RecordatorioPreventivo

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_nombre_completo', 'rut', 'telefono', 'direccion')
    search_fields = ('rut', 'usuario__first_name', 'usuario__last_name', 'telefono')

    @admin.display(description='Nombre Completo')
    def get_nombre_completo(self, obj):
        return f"{obj.usuario.first_name} {obj.usuario.last_name}"

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'especie', 'raza', 'tutor', 'numero_chip')
    list_filter = ('especie',)
    search_fields = ('nombre', 'numero_chip', 'tutor__rut')

@admin.register(Veterinario)
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_nombre_completo', 'especialidad', 'licencia_medica')
    list_filter = ('especialidad',)
    search_fields = ('licencia_medica', 'usuario__first_name', 'usuario__last_name')

    @admin.display(description='Veterinario')
    def get_nombre_completo(self, obj):
        return f"Dr(a). {obj.usuario.first_name} {obj.usuario.last_name}"

@admin.register(CitaMedica)
class CitaMedicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'mascota', 'veterinario', 'fecha_hora', 'estado')
    list_filter = ('estado', 'fecha_hora')
    search_fields = ('mascota__nombre', 'motivo')
    date_hierarchy = 'fecha_hora'

@admin.register(FichaMedica)
class FichaMedicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'mascota', 'cita', 'diagnostico')
    search_fields = ('mascota__nombre', 'diagnostico', 'tratamiento')

@admin.register(RecordatorioPreventivo)
class RecordatorioPreventivoAdmin(admin.ModelAdmin):
    list_display = ('id', 'mascota', 'tipo', 'fecha_proxima', 'notificacion_enviada')
    list_filter = ('tipo', 'notificacion_enviada')
    search_fields = ('mascota__nombre', 'descripcion')