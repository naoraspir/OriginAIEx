from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from uvicorn import run
from Schemes import TranslationRequest, TranslationResponse
from Translator import Translator
import os
from ValidationsUtills import validate_requset

# Initialize the FastAPI app
app = FastAPI()
origins = ["*"]
methods = ["*"]
headers = ["*"]

# Enable later integration to API Gateway
app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers    
)

# We will follow the requests from when the service is initialized and inform the user
request_id_counter = 0

# We will initialize 2 specific translator for our specif tasks , one Hebrew to Russian and one Russian to Hebrew
# And one English to Hebrew. We initialize once at the start of the program and use it as many times as we want.(optimization)
heb_rus = Translator("he", "ru")
eng_heb = Translator("en", "he")

# We will now create a dictionary to make the mapping from arriving source language to the correct translator.
tranlator = {
    "hebrew": heb_rus,
    "english": eng_heb
}

# We use the amazing async functionality that fastapi provides to make our code run faster.
@app.get("/")
async def root():
    return {"message": "Welcome to the OriginAI Translator API!"}

@app.post("/translate", response_model=TranslationResponse)
async def get_translation(body: TranslationRequest):
    # Validation of the request body is served from the Schemes.py file
    # We will now check the rquest
    if validate_requset(body): 
        translated = str(tranlator[body.src_lang.lower()].translate(body.src_text))# We will not support batch translate in this version but it ready
        global request_id_counter
        request_id_counter += 1
        trg_lang = body.trg_lang
        if trg_lang == None:
            return{
                "src_text" : body.src_text,
                "trg_text" : translated,
                "request_id" : request_id_counter
            }
        else:    
            return {
                "src_text" : body.src_text,
                "trg_text" : translated,
                "trg_lang" : body.trg_lang,
                "request_id" : request_id_counter
            }
    else:
        raise HTTPException(status_code=400, detail="Server error")
    
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	run(app, host="0.0.0.0", port=port)