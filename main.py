from fastapi import FastAPI
from routes.entry import entry_route 

app = FastAPI()

app.include_router(entry_route)
