from project.main_page import app

def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, World!"


def test_displayMainPage():
    tester = app.test_client()
    response = tester.get("/main_page", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Main Page"

