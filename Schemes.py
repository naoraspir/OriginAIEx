from typing import Optional
from pydantic import BaseModel

# These classes are used to validate the request and response data by FastAPI and Pydantic
class TranslationRequest(BaseModel):
    src_text: str
    src_lang: str
    trg_lang: Optional[str] = None

class TranslationResponse(BaseModel):
    src_text: str
    trg_text: str
    trg_lang: Optional[str] = "Not specified"
    request_id: int