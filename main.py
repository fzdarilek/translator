from GttsTranslations import chinese_to_pinyin, translate_to_english, detect_language, speak_text_with_gTTS
from GetText import get_text_from_image_file
from GetImage import get_image
from AddWords import add_to_chi_words_file
import keyboard

if __name__ == "__main__": 
    while True:
        if keyboard.is_pressed("'"):
            get_image()
            file = "screenshot.png"
            text = get_text_from_image_file(file)
            
            if text:
                lang = detect_language(text)
                pinyin = chinese_to_pinyin(text)
                eng = translate_to_english(pinyin)
                
                print("Original text: " + text)
                print("Detected language: " + lang)
                
                if lang == "zh-CN":  # Check if the detected language is Chinese
                    with open("chi_words.txt", "r", encoding="utf-8") as f:
                        chi_words = set(line.split("(")[0].strip() for line in f)
                        print("Existing Chinese words:", chi_words)
                    if text not in chi_words:
                        print("Adding word:", text)
                        add_to_chi_words_file(text, pinyin, eng)
                
                print("Text in pinyin: " + pinyin)
                print("Text in English: " + eng)
                
                speak_text_with_gTTS(text, lang)
                speak_text_with_gTTS(eng)
            else:
                speak_text_with_gTTS("Sorry, couldn't get the chosen text.")    