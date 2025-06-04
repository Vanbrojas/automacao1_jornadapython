import pyautogui
import time

pyautogui.position()  # Obtém a posição atual do mouse
time.sleep(5)  # Aguarda 2 segundos para que o usuário possa posicionar o mouse
print(pyautogui.position())  # Exibe a posição do mouse no console