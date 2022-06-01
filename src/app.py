from fastapi import FastAPI

from src.routers import rooms


def create_app() -> FastAPI:
    app = FastAPI(title="CustomLogger", debug=True)
    return app


app = create_app()
app.include_router(rooms.router, tags=["Meeting Room"])
