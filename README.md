# Ingresos y Gastos Mensuales

API REST construida con Django y Django REST Framework para registrar categorías, ingresos y gastos mensuales. El servicio expone endpoints autenticados con JWT, permite filtrar y ordenar transacciones, y está preparado para desplegarse en plataformas que usen `gunicorn` y ficheros estáticos servidos con WhiteNoise.

## Características principales
- CRUD completo de categorías, ingresos y gastos (expensas) vía `ModelViewSet`.
- Autenticación basada en JSON Web Tokens usando `djangorestframework-simplejwt`.
- Filtros y ordenamientos por categoría, fecha y monto a través de `django-filter`.
- CORS configurable por entorno y middleware listo para clientes SPA (React, Vue, etc.).
- Configuración de base de datos flexible con `dj-database-url` (SQLite por defecto, soporte para PostgreSQL en producción).
- Servido estático optimizado con WhiteNoise y compatibilidad con despliegues tipo Heroku (Procfile).

## Pila tecnológica
- Python 3.12+
- Django 5.2
- Django REST Framework 3.16
- SimpleJWT 5.5
- django-filter, django-cors-headers
- WhiteNoise y Gunicorn

## Estructura del proyecto

```
├── IngresosyGastosMensuales/     # Configuración base de Django
│   ├── settings.py               # Ajustes generales, REST Framework, JWT, CORS
│   └── urls.py                   # Rutas globales y endpoints de autenticación
├── expensas/                     # App principal con modelos y vistas de la API
│   ├── models.py                 # Category, Ingresos y Gastos
│   ├── views.py                  # ViewSets con filtros y permisos
│   └── serializers.py            # Serializadores DRF
├── staticfiles/                  # Directorio de estáticos recolectados (generado)
├── API.md                        # Referencia puntual de endpoints y ejemplos
├── requirements.txt              # Dependencias del proyecto
├── Procfile                      # Comando de arranque con Gunicorn
└── manage.py
```

## Requisitos previos
- Python 3.12 o superior.
- `pip` y `virtualenv` (recomendado).
- Opcional: PostgreSQL si se usará en producción.

## Puesta en marcha local

1. **Clonar el repositorio**  
   ```bash
   git clone <url-del-repo>
   cd TrabajoFinalDesarrollo
   ```

2. **Crear y activar un entorno virtual**  
   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Linux / macOS
   .\.venv\Scripts\activate       # Windows PowerShell
   ```

3. **Instalar dependencias**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno** (ver apartado siguiente).  
   Para desarrollo puedes crear un fichero `.env` y cargarlo con `python-dotenv` o exportarlos manualmente.

5. **Aplicar migraciones y, si lo deseas, crear un superusuario**  
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor de desarrollo**  
   ```bash
   python manage.py runserver
   ```
   La API estará disponible en `http://localhost:8000/`.

## Variables de entorno

| Variable | Descripción |
|----------|-------------|
| `SECRET_KEY` | Clave secreta de Django (obligatoria en producción). |
| `DEBUG` | `1` para modo desarrollo, `0` para producción. |
| `ALLOWED_HOSTS` | Lista separada por comas de hosts permitidos (p.ej. `localhost,miapp.com`). |
| `CSRF_TRUSTED_ORIGINS` | URLs confiables para CSRF, separadas por comas. |
| `CORS_ALLOWED_ORIGINS` | Orígenes permitidos para CORS, separadas por comas. Valor por defecto: `http://localhost:3000,http://localhost:5173`. |
| `DATABASE_URL` | URL de conexión (ej.: `postgres://usuario:clave@host:puerto/db`). Si se omite, se usa SQLite (`db.sqlite3`). |

> Consejo: en producción, combina `DATABASE_URL`, `SECRET_KEY`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS` y `CORS_ALLOWED_ORIGINS` para un despliegue seguro.

## Autenticación y consumo de la API

1. Obtén un token de acceso con `POST /api/token/` enviando usuario y contraseña.
2. Usa el valor `access` en la cabecera `Authorization: Bearer <token>`.
3. Renueva el token con `POST /api/token/refresh/` cuando sea necesario.

Los endpoints principales están documentados en `API.md`, incluyendo filtros (`category`, `date`), ordenamientos (`ordering`) y ejemplos concretos con `curl`.

## Despliegue

- El proyecto incluye un `Procfile` con `web: gunicorn IngresosyGastosMensuales.wsgi:application`.
- WhiteNoise está habilitado para servir archivos estáticos; ejecuta `python manage.py collectstatic` antes de subir a producción.
- Configura `DATABASE_URL`, `SECRET_KEY`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS` y `CORS_ALLOWED_ORIGINS` en la plataforma de despliegue.
- Si usas PostgreSQL, asegúrate de tener instalado `psycopg2-binary` (incluido en `requirements.txt`).

## Recursos adicionales

- Documentación detallada de endpoints: consulta `API.md`.
- Panel de administración de Django disponible en `/admin/` (requiere superusuario).
- Ajustes de internacionalización preconfigurados en español (`es-ar`) y huso horario `America/Buenos_Aires`.

