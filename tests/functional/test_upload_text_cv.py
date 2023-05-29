"""Upload text CV feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario("upload_cv_text.feature", "Uploading text")
def test_uploading_text():
    """Uploading text."""


@given("I'm a job seeker")
def given_job_seeker():
    pass  # no validations for now. Registered users will be checked with DB later


@given("I have text of the CV")
def given_cv_text():
    return create_test_cv_text()


@when("I go to the main page")
def when_main_page():
    pass


@when("I paste text in the CV section")
def when_paste_cv_text():
    pass


@when("I press 'Upload' button")
def when_press_upload_button():
    pass


@then("I should not see the error message")
def then_no_error_message():
    pass


@then("the CV should be uploaded")
def then_cv_uploaded():
    pass


def create_test_cv_text():
    return "cv text"
