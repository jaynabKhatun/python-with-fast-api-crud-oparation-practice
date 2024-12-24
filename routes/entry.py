from fastapi import APIRouter

entry_route = APIRouter()

# Api endpoint


@entry_route.get('/')
def rootApiRunner():
    response = {
        "status": "Ok",
        "status-code": 200,
        "message": "Api is running"
    }
    return response
