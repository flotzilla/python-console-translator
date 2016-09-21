import sys
import os

from src.Translator import Translator
from src.System import System

system = System(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             'config/settings.conf'))
translator = Translator()

# Read input params
if len(sys.argv) > 1:

    # if you wanna to enter to interactive mode
    if sys.argv[1] == '-i':
        print("interactive mode")

    # just translate one sentence
    else:
        max_i = len(sys.argv)
        text = ""

        for i in range(1, max_i):
            text += sys.argv[i] + " "

        to_lang = translator.determine_lang(text)
        translation = translator.get_yandex_translate(text, to_lang)

        if system.is_save_to_file:
            if to_lang == "ru":
                system.save_to_file(text, translation)
            elif to_lang == "en":
                system.save_to_file(translation, text)

elif len(sys.argv) == 1:
    print("Nothing to translate")
