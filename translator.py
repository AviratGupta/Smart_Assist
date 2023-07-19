from deep_translator import (GoogleTranslator,PonsTranslator,LingueeTranslator,MyMemoryTranslator,YandexTranslator,DeeplTranslator,QcriTranslator,single_detection,batch_detection)

def translator(text,input_lang,output_lang):
    langs_list = GoogleTranslator().get_supported_languages()
    langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
    # lang = single_detection('bonjour la vie', api_key='368b15125d64ccaf6395737f8765d47b')
    # lang = batch_detection(['bonjour la vie', 'hello world'], api_key='368b15125d64ccaf6395737f8765d47b')
    translated = GoogleTranslator(source=input_lang, target=output_lang).translate(text=text)
    return translated