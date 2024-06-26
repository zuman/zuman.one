# zuman.one
Source code to my personal website !

[zuman.one](https://zuman.one)

## Setup notes:
### 1. Create a **.env** file in **root** directory similar to the one mentioned below.

>**.env**
```
SECRET_KEY=...
SALT=...
PORT=...
SERVER_NAME=...
COMPOSE_PROJECT_NAME=...
LOG_LEVEL=...
#DEBUG, INFO, WARNING, ERROR, CRITICAL

SQLALCHEMY_DATABASE_URI=...
POSTGRES_PASSWORD=...

SESSION_TYPE=memcached
SESSION_MEMCACHED=...<Value from COMPOSE_PROJECT_NAME>...-mc-1:11211
SESSION_COOKIE_NAME=...
SESSION_COOKIE_SECURE=False
# True for production
PERMANENT_SESSION_LIFETIME=86400
# Any integer to denote seconds

REMEMBER_COOKIE_DURATION=2592000
# Any integer to denote seconds
REMEMBER_COOKIE_HTTPONLY=True
REMEMBER_COOKIE_SECURE=False
# True for production

MAIL_USERNAME=...
MAIL_PASSWORD=...

FLASK_APP=main.py
FLASK_ENV=...
FLASK_DEBUG=...
# 0 for production, 1 for development

DOCKER_DEFAULT_PLATFORM=linux/amd64
```

### 2. Build image and run docker compose

```
export POSTGRES_PASSWORD=... # from .env
export COMPOSE_API_NAME=...-api-1 # Use COMPOSE_PROJECT_NAME from .env (Don't forget to append "-api-1")
export FLASK_ENV=... # from .env
docker build api -t one.zuman.api:$FLASK_ENV
docker compose up -d
```

### 3. Initialize the database

```
docker exec -it $COMPOSE_API_NAME sh /app/db-sync
```

### 4. Create a proxy server from [common-proxy](https://github.com/zuman/common-proxy)

### 5. Restart the stack
```
docker build api -t one.zuman.api:$FLASK_ENV     # If you recently changed the code
docker compose down
docker compose up -d
```
