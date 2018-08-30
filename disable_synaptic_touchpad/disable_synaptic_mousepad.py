from pyautogui import hotkey, press
import win32gui, win32con
import re
import os
import time


class WindowManager:
    """"""
    
    def __init__(self):
        self._handle = None
        
    def _window_enum_callback(self, hwnd, wildcard):
        # print("hwnd: {}, wildcard: {}".format(hwnd, wildcard))
        """Pass to win32gui.EnumWindows() to check all opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            # print("hwnd: {}, wildcard: {}, win32gui: {}".format(
                # hwnd, wildcard, win32gui.GetWindowText(hwnd)
            # ))
            self._handle = hwnd
            
    def find_window_wildcard(self, wildcard):
        """Find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)
        
    def set_foreground(self):
        """Put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)
        
    def close_window(self):
        """Close the current window"""
        if self._handle is not None:
            win32gui.SendMessage(self._handle, win32con.WM_CLOSE, 0, 0)


# Ask if user wants to disable or enable mousepad
user_input = input("[d]isable or [e]nable? ")
user_input = user_input.strip().lower()

# Open mouse control panel
os.system('main.cpl')

time.sleep(1)

# Find the Mouse Properties window
w = WindowManager()
w.find_window_wildcard("Mouse Properties")
w.set_foreground()

# Go to last tab
hotkey('ctrl', 'shift', 'tab')

# Enable/disable mousepad depending on the user input
if user_input == "d" or user_input == "disable":
    hotkey('alt', 'd')
    time.sleep(0.5)
    press("enter")
    time.sleep(0.5)
    press("enter")
elif user_input == "e" or user_input == "enable":
    hotkey('alt', 'e')
    time.sleep(0.5)
    press("enter")
    time.sleep(0.5)
    press("enter")
else:
    print("Invalid user input")
    
w.close_window()
