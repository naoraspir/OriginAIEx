# regular expression patterns
HebOnly = r'^[0-9\u0590-\u05FF\s\u0590-\u05FF\s.,!?\'\"\(\)]*$'
EngOnly = r'^[a-zA-Z0-9\s.,!?\'\"\(\)]*$'

#supported languages
src_languages = ["hebrew", "english"]
trg_languages = ["hebrew", "russian"]