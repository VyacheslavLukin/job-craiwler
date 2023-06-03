import pytest
from src.client_api.models import CVModel

test_cv = CVModel(content="cv text")


def test_should_return_error_if_len_more_than_1000_words():
    with pytest.raises(ValueError):
        CVModel(content="word" * 1001)


def test_should_return_error_if_no_content():
    with pytest.raises(ValueError):
        CVModel(content="")
