from pydantic import BaseModel


class CreateTaskResponse(BaseModel):
    task_id: str
    status: str


class OCRResponse(BaseModel):
    read_text: str | None = None
    status: str
