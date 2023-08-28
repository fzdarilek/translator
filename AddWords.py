def add_to_chi_words_file(word, pinyin, translation):
    with open("chi_words.txt", "a", encoding="utf-8") as f:
        f.write(f"{word}({pinyin}) => {translation}\n")