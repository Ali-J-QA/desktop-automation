# calculator.py
import pyautogui
import subprocess
import time
import pyperclip  # To handle clipboard actions

class WindowsCalculator:
    def __init__(self):
        self.calculator_process = None

    def open_calc(self):
        """Launch the Windows Calculator."""
        self.calculator_process = subprocess.Popen("calc.exe")
        time.sleep(2)

    def press(self, key):
        """Press a specific key."""
        pyautogui.write(str(key))
        time.sleep(0.5)

    def press_enter(self):
        """Press Enter."""
        pyautogui.press('enter')
        time.sleep(1)

    def press_copy(self):
        """Press Ctrl + C to copy the calculator's display result."""
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)

    def close_calc(self):
        """Close the calculator."""
        pyautogui.hotkey('alt', 'f4')
        time.sleep(1)

    def perform_calculation(self, calculation):
        """Perform a calculation (e.g., '2 + 2')."""
        for key in calculation:
            self.press(key)
        self.press_enter()

    def get_result_from_clipboard(self):
        """Get the result from the calculator's display using the clipboard."""
        self.press_copy()  # Copy the result to clipboard
        result = pyperclip.paste()  # Get the clipboard content
        return result.strip()
