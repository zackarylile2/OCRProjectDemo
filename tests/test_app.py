from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_start_ocr_task():
    response = client.post(
        "/start-ocr-task", files={"file": ("test.png", b"fakeimagebytes", "image/png")}
    )
    assert response.status_code == 200
    assert "task_id" in response.json()
    assert response.json()["status"] == "processing"
