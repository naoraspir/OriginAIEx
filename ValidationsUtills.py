# Validations utills for text fields and languages
from fastapi import HTTPException
import regex
from consts import EngOnly, HebOnly, src_languages, trg_languages

def validate_source_lang(lang):
    #check if the source language is supported
    if lang.lower() not in src_languages:
        raise HTTPException(status_code=404, detail="Source language not supported")
    else:
        return

def validate_trg_lang(lang):
    #check if the target language is supported
    if lang !=None and lang.lower() not in trg_languages :
        raise HTTPException(status_code=404, detail="Target language not supported")
    else:
        return

def validate_text(text, source_lang):
    source_lang = source_lang.lower()
    #check if the text is not empty and if it matches the source language
    if text == "":
        raise HTTPException(status_code=400, detail="No text to translate")
    #check if the text is in the correct language
    elif source_lang == "hebrew":
        if regex.match(HebOnly, text):
            return True
        else:
            raise HTTPException(status_code=400, detail="Source text does not match source language")
    elif source_lang == "english":
        if regex.match(EngOnly, text):
            return True
        else:
            raise HTTPException(status_code=400, detail="Source text does not match source language")
    
    else:
        raise HTTPException(status_code=404, detail="Source language not supported")

def validate_requset(request):
    #check if the request is valid
    src_text = request.src_text
    src_lang = request.src_lang
    trg_lang = request.trg_lang

    validate_source_lang(src_lang)
    validate_trg_lang(trg_lang)

    return validate_text(src_text, src_lang)