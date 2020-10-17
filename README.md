
# API

Build with dev container in VsCode

## How to test?

GET

```bash
curl http://localhost:8000/api/v1/videos
```

POST

```bash
curl -X POST http://localhost:8000/api/v1/videos -H "Content-Type: application/json" -d '{"title": "Nuevo Video", "description": "Una breve descripcion", "slug": "nuevo-video"}'
```

GET Id

```bash
curl http://localhost:8000/api/v1/videos/1 -I
```

PUT

```bash
curl -X PUT http://localhost:8000/api/v1/videos/2 -H "Content-Type: application/json" -d '{"title": "Nuevo título", "description": "Una nueva descripcion", "slug": "nuevo-video"}'
```

DELETE

```bash
curl -X DELETE http://localhost:8000/api/v1/videos/2
```
