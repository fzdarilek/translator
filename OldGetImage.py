import time
from pynput.mouse import Listener
import pyautogui
from pynput import mouse
from GttsTranslations import speak_text_with_gTTS

left_clicks = 0
x1, y1, x2, y2 = None, None, None, None

def swap_if_needed(x1, y1, x2, y2):
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    return x1, x2, y1, y2
        
def on_click(x, y, button, pressed_time):
    global left_clicks, x1, y1, x2, y2
    if button == mouse.Button.left:
        if pressed_time >= 1.0:  
            if left_clicks == 0:
                x1, y1 = pyautogui.position()
                speak_text_with_gTTS("First corner.")
            elif left_clicks == 1:
                x2, y2 = pyautogui.position()
                speak_text_with_gTTS("Second corner.")
                swap_if_needed(x1, y1, x2, y2)
                region = (x1, y1, x2 - x1, y2 - y1)
                im = pyautogui.screenshot(region=region)
                grayscale_screenshot = im.convert('L')
                grayscale_screenshot.save('screenshot.png')
                left_clicks = 0
                return False

            left_clicks += 1
        else:
            print("so biib")

def monitor_mouse():
    start_time = None

    def on_press(x, y, button, pressed):
        nonlocal start_time
        if button == mouse.Button.left:
            if pressed:
                start_time = time.time()
            else:
                if start_time is not None:
                    pressed_time = time.time() - start_time
                    if on_click(x, y, button, pressed_time) is False:
                        return False  
                    start_time = None

    with Listener(on_click=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    monitor_mouse()
