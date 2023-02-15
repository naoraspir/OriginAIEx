from transformers import AutoTokenizer, TFMarianMTModel
# The loading of the model and the tokenizer is done only once per language pair.
# It is done to optimize the code and make it run faster.(bound by the loading time of the model)
# Better to seprete this logic to conduct mock tests.
def load_model(model_name):
    model = TFMarianMTModel.from_pretrained(model_name)
    return model

def load_tokenizer(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return tokenizer 

class Translator:
    '''
    This class is used to translate text from one language to another.
    The class is initialized with the source language and the target language.
    The class has a method called translate that takes a string and returns a string.
    '''
    def __init__(self, src, trg):
        # We will now check the source and target language and initialize the correct model and tokenizer.
        if src == "en" and trg == "he":
            self.lang = "english"
        elif src == "he" and trg == "ru":
            self.lang = "hebrew"
        else:
            raise ValueError("Source/Target language pair not supported")
        # We will now load the model and the tokenizer and save them as attributes of the class.
        self.src = src
        self.trg = trg
        self.model_name = f"Helsinki-NLP/opus-mt-{src}-{trg}"
        self.model = load_model(self.model_name)
        self.tokenizer = load_tokenizer(self.model_name)
        
        return

    def translate(self, text: str) -> str:
        # This is the actual inference method.
        if type(text) != str:
            raise TypeError("Input must be a string")
        batch = self.tokenizer([text], return_tensors="tf")
        gen = self.model.generate(**batch)
        res = self.tokenizer.batch_decode(gen, skip_special_tokens=True)
        
        return res[0]