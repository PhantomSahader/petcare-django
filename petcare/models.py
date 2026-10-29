from django.db import models
from django.contrib.auth.models import User

# 1. Perfil del Tutor (Tutores de las mascotas)
class Tutor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_tutor')
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name} ({self.rut})"


# 2. Paciente / Mascota
class Mascota(models.Model):
    ESPECIES = [
        ('PERRO', 'Perro'),
        ('GATO', 'Gato'),
        ('EXOTICO', 'Exótico'),
    ]
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='mascotas')
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=20, choices=ESPECIES)
    raza = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    numero_chip = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - Tutor: {self.tutor.usuario.last_name}"


# 3. Personal Veterinario
class Veterinario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_veterinario')
    especialidad = models.CharField(max_length=100)
    licencia_medica = models.CharField(max_length=50)

    def __str__(self):
        return f"Dr(a). {self.usuario.first_name} {self.usuario.last_name} - {self.especialidad}"


# 4. Agendamiento y Control de Citas Médicas
class CitaMedica(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADA', 'Confirmada'),
        ('ATENDIDA', 'Atendida'),
        ('CANCELADA', 'Cancelada'),
    ]
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='citas')
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, related_name='citas')
    fecha_hora = models.DateTimeField()
    motivo = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')

    def __str__(self):
        return f"Cita: {self.mascota.nombre} con {self.veterinario} ({self.fecha_hora.strftime('%d/%m/%Y %H:%M')})"


# 5. Ficha Médica Clínica Completa
class FichaMedica(models.Model):
    cita = models.OneToOneField(CitaMedica, on_delete=models.CASCADE, related_name='ficha')
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='fichas')
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    receta = models.TextField(blank=True, null=True)
    examenes_sugeridos = models.TextField(blank=True, null=True)
    fecha_atencion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ficha Médica #{self.id} - Mascota: {self.mascota.nombre}"


# 6. Módulo Automatizado de Recordatorios
class RecordatorioPreventivo(models.Model):
    TIPOS = [
        ('VACUNA', 'Vacunación'),
        ('DESPARASITACION', 'Desparasitación'),
        ('CONTROL', 'Control Sanitario'),
    ]
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='recordatorios')
    tipo = models.CharField(max_length=20, choices=TIPOS)
    descripcion = models.CharField(max_length=150)
    fecha_aplicacion = models.DateField()
    fecha_proxima = models.DateField()
    notificacion_enviada = models.BooleanField(default=False)

    def __str__(self):
        return f"Recordatorio: {self.get_tipo_display()} para {self.mascota.nombre} ({self.fecha_proxima})"