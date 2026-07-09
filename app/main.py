from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI(
    title="Inframind API 🚀",
    version="2.0.0"
)


VERSION = "v2 - deploy automático con Cloud Build"


@app.get("/")
def home():
    return {
        "message": "🔥 Nueva versión desplegada",
        "version": VERSION,
        "deployed_at": datetime.now().isoformat(),
        "container": os.getenv("HOSTNAME")
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "inframind-api"
    }


@app.get("/test")
def test():
    return {
        "mensaje": "Cambio realizado desde Git → Cloud Build → Cloud Run 🚀"
    }