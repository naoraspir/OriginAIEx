import Translator as tr
import pytest

def create_mock_translator(monkeypatch: pytest.MonkeyPatch) -> tr.Translator:
    monkeypatch.setattr(tr, "load_model", lambda x: None)
    monkeypatch.setattr(tr, "load_tokenizer", lambda x: None)
    return tr.Translator("he", "ru")


def test_valid_translator_init(monkeypatch: pytest.MonkeyPatch) -> None:
    mock_heb_rus = create_mock_translator(monkeypatch)
    assert mock_heb_rus.lang == "hebrew"
    assert mock_heb_rus.src == "he"
    assert mock_heb_rus.trg == "ru"
    assert mock_heb_rus.model_name == "Helsinki-NLP/opus-mt-he-ru"
    assert mock_heb_rus.model == None
    assert mock_heb_rus.tokenizer == None

def test_invalid_translator_init() -> None:
    with pytest.raises(ValueError):
        tr.Translator("en", "ru")

def test_not_str_translate(monkeypatch: pytest.MonkeyPatch) -> None:
    mock_heb_rus = create_mock_translator(monkeypatch)
    with pytest.raises(TypeError):
        mock_heb_rus.translate(123)