from fastapi import Depends, FastAPI
from .socket.main import socket_app

from .db.main import engine
from .router.v1 import usersRoute, authRoute,adminRoute,shopRoute,postsRoute

app = FastAPI()



@app.get("/", tags=["Main"])
async def read_root():
    return {"Hello": "World"}

app.include_router(adminRoute.router)
app.include_router(authRoute.router)
app.include_router(usersRoute.router)
app.include_router(shopRoute.router)
app.include_router(postsRoute.router)
app.mount(path="/",app=socket_app)


