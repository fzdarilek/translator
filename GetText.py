import pytesseract

def read_text_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        return text.strip()
    except Exception as e:
        print("Error occurred while reading the file:", e)
        return None
    

def get_text_from_image_file(image_file_path):
    try:
        text = pytesseract.image_to_string(image_file_path, lang="chi_sim")
        return text.strip()
    except Exception as e:
        print("Error occurred while extracting text:", e)
        return None