from fastapi import FastAPI
from contextlib import asynccontextmanager

import uvicorn

from core.config import settings
from core.models import Base, db_helper
from items_views import router as items_router
from users.views import router as users_router
from api_v1 import router as router_v1 


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_router)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get('/')
def hello_index():
    return {"message": "Hello index!"}


@app.get('/hello/')
def get_hello(name: str):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)
    
