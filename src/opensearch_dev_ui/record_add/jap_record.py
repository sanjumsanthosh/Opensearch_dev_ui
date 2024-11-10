from pydantic import BaseModel

class JapRecord(BaseModel):
    title: str
    text: str
    # site_id defautl to 10, answer_id defaults to 10
    site_id: int = 10
    answer_id: int = 10