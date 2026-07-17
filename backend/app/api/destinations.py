from fastapi import APIRouter

router = APIRouter(prefix="/destinations", tags=["Destinations"])

destinations = [
    {
        "id": 1,
        "name": "Home",
        "address": "Lucknow"
    },
    {
        "id": 2,
        "name": "Office",
        "address": "Noida"
    }
]

@router.get("/")
async def get_destinations():
    return destinations