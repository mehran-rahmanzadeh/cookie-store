# Save user data in cookie (unauthorized)
### Stack
- Python 3.8
- Django 3.2

### Description
This application allows users to use a demo version of the application.

### Running
- Copy sample config
```bash
cp docs/docker/settings.ini .
```
- Build
```bash
docker compose up -d --build
# or in older version: docker-compose up -d
```
Possible issues:
- if you can not log in to admin panel, try to create superuser in `demo_django` container
### Usage
You can set data in session using provided API endpoint: `/api/v1/demo/data/`.