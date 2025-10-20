
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_search_long_parameter():
    # По бессмысленному запросу ожидаем 0, а по инъекции — тоже 0 (не все элементы)
    search_param = "z" * 40
    resp_noise = client.get("/search", params={"q": search_param})
    assert resp_noise.status_code in {422, 400} , "Длина q должна быть ограничена"
