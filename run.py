import uvicorn

import src.models as models
from src.app import app
from src.db import engine


models.Base.metadata.create_all(bind=engine)


def run() -> None:
    uvicorn.run(
        app,
        host="localhost",
        port=8888,
        loop="uvloop",
        lifespan="on",
    )


if __name__ == "__main__":
    run()
