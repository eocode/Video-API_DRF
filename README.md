
# API

Build with dev container in VsCode

Objective: Test Dev Containers in VsCode with an app in Django and DRG for development

## DEMO

<div align="center">
  <img src="img/1.png">
</div>

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

## How to use?

Run VsCode Dev Containers and type:

```
pip install -r requirements.txt
python manage.py runserver
```