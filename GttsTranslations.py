from gtts import gTTS
import pygame
from googletrans import Translator
import pypinyin

def chinese_to_pinyin(text):
    pinyin = pypinyin.lazy_pinyin(text)
    return ' '.join(pinyin)

def translate_to_english(text):
    translator = Translator()
    translation = translator.translate(text, src="zh-CN", dest="en")
    return translation.text

def detect_language(text):
    try:
        translator = Translator()
        lang = translator.detect(text).lang
        return lang
    except Exception as e:
        print("Error occurred while detecting language:", e)
        return None
    
def speak_text_with_gTTS(text, lang="en"):
    try:
        tts = gTTS(text=text, lang=lang)

        tts_file = "output.mp3"
        tts.save(tts_file)

        pygame.mixer.init()
        pygame.mixer.music.load(tts_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

        pygame.mixer.quit()

    except Exception as e:
        print("Error occurred while speaking:", e)
