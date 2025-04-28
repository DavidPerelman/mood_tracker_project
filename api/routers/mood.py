from fastapi import APIRouter
from api.models.mood import UserMood, UserMoodIn

router = APIRouter()


mood_table = {}


def find_mood(mood_id: int):
    return mood_table.get(mood_id)


@router.post("/moods", response_model=UserMood)
async def create_mood(mood: UserMoodIn):
    data = mood.model_dump()
    last_record_id = len(mood_table)
    new_mood = {**data, "id": last_record_id}
    mood_table[last_record_id] = new_mood
    return new_mood


@router.get("/moods", response_model=list[UserMood])
async def get_moods():
    return list(mood_table.values())


@router.get("/")
async def root():
    return {"message": "Hello World!"}
