# Registro de Uso de Inteligencia Artificial (prompts_ia.md)

**Asignatura:** Desarrollo Backend - EVA 3  
**Proyecto:** Proyecto 1 - Sistema de Gestión de Citas y Fichas Médicas (PetCare)  
**Estudiante:** Joaquín Soto Cifuentes  

---

## Prompts Utilizados y Apoyo Solicitado

### 1. Configuración del Entorno y Conexión a Base de Datos
* **Consulta:** "Cómo configurar settings.py en Django para conectar con una instancia de PostgreSQL en AWS RDS usando psycopg2."
* **Uso:** Estructuración del diccionario DATABASES y manejo de variables de entorno.

### 2. Lógica de Negocio y Serializadores (DRF)
* **Consulta:** "Crear una validación personalizada en Django REST Framework dentro de validate() o validate_fecha_hora() para evitar que un veterinario tenga citas solapadas en el mismo horario."
* **Uso:** Implementación del filtro `CitaMedica.objects.filter()` en `serializers.py`.

### 3. Diseño Frontend e Interfaz Gráfica
* **Consulta:** "Generar una plantilla HTML responsive con Tailwind CSS para un sistema de veterinaria con modales para operaciones CRUD mediante peticiones fetch a una API REST de Django."
* **Uso:** Construcción de `index.html` con gestión dinámica de estados y renderizado en DOM.

### 4. Scripts de Despliegue y Pruebas
* **Consulta:** "Crear un script en la shell de Django para poblar la base de datos con registros de prueba (Tutores, Mascotas, Citas y Fichas)."
* **Uso:** Generación rápida de datos de prueba para la defensa en vivo.