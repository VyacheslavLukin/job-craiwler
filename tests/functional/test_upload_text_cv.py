"""Upload text CV feature tests."""

from typing import Literal
from src.client_api import app
from fastapi.testclient import TestClient
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

client = TestClient(app)


@scenario("upload_cv_text.feature", "Uploading text CV")
def test_uploading_text():
    """Uploading text CV."""


@given("I'm a job seeker")
def given_job_seeker():
    raise NotImplementedError


@given("I have text of the CV")
def given_cv_text() -> Literal["cv text"]:
    return create_test_cv_text()


@when("I go to the main page")
def when_main_page():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


@when("I paste text in the CV section")
def when_paste_cv_text():
    raise NotImplementedError


@when("I press 'Upload' button")
def when_press_upload_button():
    response = client.post("/upload_text_cv", json={"content": "cv text"})
    assert response.status_code == 200
    assert response.json() == {"msg": "CV has been uploaded"}


@then("the CV should be uploaded")
def then_cv_uploaded():
    raise NotImplementedError


def create_test_cv_text() -> Literal["cv text"]:
    return "cv text"
