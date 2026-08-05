# -_- / HiVITS Backend

열심히 하겠습니다

# HiVITS Backend (FastAPI + MySQL)

Minimal CRUD API implementation using FastAPI, SQLAlchemy and MySQL.

Run (development):

1. Create a virtualenv and install dependencies:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

2. Configure database: copy `.env.example` to `.env` and set `DATABASE_URL` to your MySQL server.

3. Create the database (example MySQL):

```sql
CREATE DATABASE hivits_db;
CREATE USER 'hivits_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON hivits_db.* TO 'hivits_user'@'localhost';
```

4. Run the app:

```bash
uvicorn hivits_backend.main:app --reload
```

APIs:
- `POST /posts/` — create post
- `GET /posts/{id}` — get single post
- `GET /posts/` — list posts (query params: skip, limit)
- `PUT /posts/{id}` — update post
- `DELETE /posts/{id}` — delete post

