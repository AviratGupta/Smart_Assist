from happytransformer import HappyTextToText
from happytransformer import TTSettings
def spell_checker(text):
    happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
    args = TTSettings(num_beams=5, min_length=1)
    result = happy_tt.generate_text("grammar: {}".format(text), args=args)
    return result.text
#print(checker("my name are avirat"))