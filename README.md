# User Service

```
docker network create polls-network   # once, shared by both services
cp .env.example .env
docker-compose up --build
```
Swagger: http://localhost:8001/docs

| Method | Path | Description |
|---|---|---|
| POST | /users | Create user |
| GET | /users/{id} | Get user |
| PUT | /users/{id} | Update user |
| PUT | /users/{id}/register | Register existing user |
| DELETE | /users/{id} | Delete user (also deletes his answers in poll service) |
