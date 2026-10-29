# PetCare - Sistema de Gestión Médica Veterinaria

Sistema Fullstack/Backend desarrollado con Django, Django REST Framework y PostgreSQL sobre AWS.

## Requerimientos del Caso Atendidos
1. **CRUD de Tutores y Mascotas:** Gestión completa de pacientes y responsables.
2. **Agenda Médica:** Control de disponibilidad y prevención de solapamientos de citas por profesional.
3. **Fichas Clínicas Digitales:** Registro de diagnósticos, tratamientos, recetas y exámenes.
4. **Recordatorios Preventivos:** Control de vacunación y desparasitaciones periódicas.

## Tecnologías Utilizadas
* Python 3.13 / Django 6.1
* Django REST Framework (DRF)
* PostgreSQL (AWS RDS / EC2)
* Tailwind CSS (Interfaz Integrada)

## Instrucciones de Ejecución Local
```bash
# 1. Activar entorno virtual
venv\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Aplicar migraciones
python manage.py migrate

# 4. Iniciar servidor
python manage.py runserver