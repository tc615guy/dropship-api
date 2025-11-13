# Dropship Intelligence API

Lightweight FastAPI service for ingesting and managing candidate dropship products.

Summary
- Endpoints:
	- `POST /ingest` — create a product from an ingest request
	- `GET /candidates` — list candidate products (ordered by reviews, rating)
	- `POST /approve` — approve a candidate by id
- Database: SQLite file at `./data.db`
- Deploy: `Dockerfile` + `render.yaml` (Render)

Notes
- Several services (keyword extraction, supplier matching, margin calculation) are placeholders — your n8n workflows handle these upstream. The repo contains comments where those integrations are expected.
- The app exposes OpenAPI docs at `/docs` when running.

Run locally
1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the server:

```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

4. Health check / docs:

- Health: `GET http://localhost:8000/` → `{ "status": "ok", "message": "Dropship API running" }`
- API docs: `http://localhost:8000/docs`

Docker
1. Build the image:

```bash
docker build -t dropship-api .
```

2. Run the container (the app listens on `$PORT` in the Dockerfile):

```bash
docker run -p 10000:10000 dropship-api
```

Render
- The repository includes `render.yaml` and a `Dockerfile` configured for Render. The service will use the `$PORT` environment variable provided by Render.

Development notes
- Models use SQLAlchemy ORM and the DB file is `data.db` by default.
- If you want local supplier/keyword/margin stubs for testing, I can add lightweight implementations.

Want me to run a quick smoke test of the running API here, or add simple local stubs for the upstream integrations?  
# dropship-api