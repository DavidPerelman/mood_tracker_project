from pydantic import BaseModel


class UserMoodIn(BaseModel):
    body: str
    # mood_score: int
    # emotions: List[str]
    # reasons: List[str] = None
    # notes: str = None


class UserMood(UserMoodIn):
    id: int
