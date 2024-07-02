from operations import menu_selection
from operations import rentland
from operations import returnLand
try:
    menu_selection()
except Exception as e:
    print(f"An error occurred: {e}")
