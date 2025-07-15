import logging

from fastapi import FastAPI, HTTPException, UploadFile, status

from app.models import CreateTaskResponse, OCRResponse
from app.tasks import process_ocr

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
LOGGER = logging.getLogger(__name__)

app = FastAPI()


@app.post("/start-ocr-task", response_model=CreateTaskResponse)
async def start_ocr_task(file: UploadFile):
    content_type = file.content_type
    if content_type not in ["application/pdf", "image/jpeg", "image/png"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported file type: {content_type}. Only PDFs and image files are allowed.",
        )

    file_bytes = await file.read()
    task = process_ocr.delay(content_type, file_bytes)
    return CreateTaskResponse(task_id=task.id, status="processing")


@app.get("/ocr-result/{task_id}", response_model=OCRResponse)
async def get_ocr_result(task_id: str):
    task = process_ocr.AsyncResult(task_id)
    if task.state == "PENDING":
        return OCRResponse(status="processing")
    elif task.state == "SUCCESS":
        return OCRResponse(read_text=task.result, status="success")
    elif task.state == "FAILURE":
        LOGGER.error(f"Task {task_id} failed: {task.info}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Task failed"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unknown task state: {task.state}",
        )
