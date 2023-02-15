from fastapi import HTTPException
from Schemes import TranslationRequest
import ValidationsUtills
import pytest

def test_invalid_source_lang() -> None:
    with pytest.raises(HTTPException):
        ValidationsUtills.validate_source_lang("chinese")

def test_valid_source_lang() -> None:
    assert ValidationsUtills.validate_source_lang("hebrew") == None
    assert ValidationsUtills.validate_source_lang("english") == None

def test_invalid_trg_lang() -> None:
    with pytest.raises(HTTPException):
        ValidationsUtills.validate_trg_lang("chinese")

def test_valid_trg_lang() -> None:
    assert ValidationsUtills.validate_trg_lang("russian") == None
    assert ValidationsUtills.validate_trg_lang("hebrew") == None    

def test_invalid_text() -> None:
    with pytest.raises(HTTPException):
        ValidationsUtills.validate_text("שלום", "english")  
        ValidationsUtills.validate_text("hello", "hebrew")
        ValidationsUtills.validate_text("", "hebrew")
        ValidationsUtills.validate_text("", "english")
        ValidationsUtills.validate_text("שלום and hi", "hebrew")
        ValidationsUtills.validate_text("hello and שלום", "english")
        ValidationsUtills.validate_text("שלום and hello", "chinese")

def test_invalid_request() -> None:
    mock_invalid_request1 = TranslationRequest(src_text="שלום", src_lang="chinese", trg_lang="russian")
    mock_invalid_request2 = TranslationRequest(src_text="hello", src_lang="english", trg_lang="chinese")
    mock_invalid_request3 = TranslationRequest(src_text="שלום", src_lang="chinese")
    mock_invalid_request4 = TranslationRequest(src_text="", src_lang="english")
    mock_invalid_request5 = TranslationRequest(src_text="שלום", src_lang="hebrew", trg_lang="chinese")

    # Validation of requests schema is done with pydantic
    # So we only need to test the validation of the text

    with pytest.raises(HTTPException):
        ValidationsUtills.validate_requset(mock_invalid_request1)
        ValidationsUtills.validate_requset(mock_invalid_request2)
        ValidationsUtills.validate_requset(mock_invalid_request3)
        ValidationsUtills.validate_requset(mock_invalid_request4)
        ValidationsUtills.validate_requset(mock_invalid_request5)

def test_valid_request() -> None:
    mock_valid_request1 = TranslationRequest(src_text="שלום", src_lang="hebrew", trg_lang="russian")
    mock_valid_request2 = TranslationRequest(src_text="hello", src_lang="english", trg_lang="hebrew")
    mock_valid_request3 = TranslationRequest(src_text="שלום", src_lang="hebrew")
    mock_valid_request4 = TranslationRequest(src_text="hello", src_lang="english")
    mock_valid_request5 = TranslationRequest(src_text="123 שלום", src_lang="hebrew", trg_lang="russian")
    mock_valid_request6 = TranslationRequest(src_text="hello 123", src_lang="english", trg_lang="hebrew")

    assert ValidationsUtills.validate_requset(mock_valid_request1) == True
    assert ValidationsUtills.validate_requset(mock_valid_request2) == True
    assert ValidationsUtills.validate_requset(mock_valid_request3) == True
    assert ValidationsUtills.validate_requset(mock_valid_request4) == True
    assert ValidationsUtills.validate_requset(mock_valid_request5) == True
    assert ValidationsUtills.validate_requset(mock_valid_request6) == True
