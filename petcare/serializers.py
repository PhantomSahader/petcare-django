from rest_framework import serializers
from .models import Tutor, Mascota, Veterinario, CitaMedica, FichaMedica, RecordatorioPreventivo

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'


class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = '__all__'


class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = '__all__'


class CitaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitaMedica
        fields = '__all__'

    def validate(self, data):
        veterinario = data.get('veterinario')
        fecha_hora = data.get('fecha_hora')

        # Regla de negocio: Evitar solapamiento de citas para el mismo profesional
        citas_existentes = CitaMedica.objects.filter(
            veterinario=veterinario,
            fecha_hora=fecha_hora,
            estado__in=['PENDIENTE', 'CONFIRMADA']
        )

        if self.instance:
            citas_existentes = citas_existentes.exclude(pk=self.instance.pk)

        if citas_existentes.exists():
            raise serializers.ValidationError(
                {"fecha_hora": "El veterinario ya tiene una cita agendada en esa fecha y hora."}
            )
        return data


class FichaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichaMedica
        fields = '__all__'


class RecordatorioPreventivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordatorioPreventivo
        fields = '__all__'