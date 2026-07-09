from fastapi import FastAPI

app = FastAPI(
        title="Inframind",
        version="1.0.0"
)

@app.get("/")
def inicio():
        return {
                "mensaje": "Bienvenido a Inframind"
                }