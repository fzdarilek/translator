import os
import keyboard
import pyperclip
from PIL import ImageGrab,ImageEnhance
import time 

def preprocess_image(image):
    # Convert to grayscale
    gray_image = image.convert("L")
    
    # Enhance contrast
    enhanced_image = ImageEnhance.Contrast(gray_image).enhance(2.0)
    
    # Apply binary thresholding
    threshold_image = enhanced_image.point(lambda p: p > 150 and 255)
    
    return threshold_image

def get_image():
    # Specify the key you want to trigger the screenshot
    trigger_key = "'"

    # Get the script's current directory
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # Simulate Windows key + Shift + S
    pyperclip.copy("")  # Clear clipboard to prevent any previous content interference
    keyboard.press('win+shift+s')
    keyboard.release('win+shift+s')
    time.sleep(10)
    
    # Get image data from clipboard and save it
    clipboard_image = ImageGrab.grabclipboard()
    if clipboard_image:
        preprocessed_image = preprocess_image(clipboard_image)
        
        # Save preprocessed image for debugging (optional)
        preprocessed_path = os.path.join(script_directory, "preprocessed.png")
        preprocessed_image.save(preprocessed_path)
        
        screenshot_filename = "screenshot.png"
        screenshot_path = os.path.join(script_directory, screenshot_filename)
        preprocessed_image.save(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")
    else:
        print("No screenshot found in clipboard.")
                