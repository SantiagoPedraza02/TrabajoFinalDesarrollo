# API de Ingresos y Gastos

- Base URL: `/api/`
- Autenticación: JWT Bearer (SimpleJWT). Obtén el token con `POST /api/token/` y usa el `access` en el header `Authorization: Bearer <token>`.

## Autenticación
- `POST /api/token/`
  - Body: `{ "username": "<usuario>", "password": "<clave>" }`
  - Respuesta: `{ "access": "...", "refresh": "..." }`
- `POST /api/token/refresh/`
  - Body: `{ "refresh": "<refresh_token>" }`
  - Respuesta: `{ "access": "..." }`

## Recursos y Endpoints

### Categorías
- Lista / crea: `GET | POST /api/categorias/`
- Detalle / actualiza / elimina: `GET | PUT | PATCH | DELETE /api/categorias/{id}/`
- Búsqueda: `GET /api/categorias/?search=<texto>` (busca por nombre)

### Ingresos
- Lista / crea: `GET | POST /api/ingresos/`
- Detalle / actualiza / elimina: `GET | PUT | PATCH | DELETE /api/ingresos/{id}/`
- Filtros: `category=<id>`, `date=<YYYY-MM-DD>`
- Orden: `ordering=date|amount` (usar `-` para descendente, por defecto: `-date`)

### Gastos (expensas)
- Lista / crea: `GET | POST /api/expensas/`
- Detalle / actualiza / elimina: `GET | PUT | PATCH | DELETE /api/expensas/{id}/`
- Filtros: `category=<id>`, `date=<YYYY-MM-DD>`
- Orden: `ordering=date|amount` (usar `-` para descendente, por defecto: `-date`)

Nota: La ruta del recurso de gastos es `expensas`.

## Esquemas de datos

### Category
- Campos: `id`, `name`, `type` (`ingresos` | `gastos`)

### Ingresos
- Campos: `id`, `amount` (decimal), `date` (YYYY-MM-DD), `description` (opcional), `category` (id de Category)

### Gastos
- Campos: `id`, `amount` (decimal), `date` (YYYY-MM-DD), `description` (opcional), `category` (id de Category)

## Ejemplos rápidos

- Obtener token (PowerShell):
  - `curl -Method POST -Uri http://localhost:8000/api/token/ -Headers @{'Content-Type'='application/json'} -Body '{"username":"admin","password":"admin"}'`
- Listar ingresos ordenados por monto descendente:
  - `curl -H "Authorization: Bearer <access>" "http://localhost:8000/api/ingresos/?ordering=-amount"`
- Crear gasto:
  - `curl -X POST -H "Authorization: Bearer <access>" -H "Content-Type: application/json" -d '{"amount": 1200.50, "date": "2025-01-15", "description": "Alquiler", "category": 3}' http://localhost:8000/api/expensas/`

## Códigos de estado esperados
- 200 OK, 201 Created, 204 No Content
- 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found

