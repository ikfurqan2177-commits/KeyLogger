from pynput.keyboard import Listener
Listener(on_press=lambda k : print(k)).start();input("Press Enter To exit....)