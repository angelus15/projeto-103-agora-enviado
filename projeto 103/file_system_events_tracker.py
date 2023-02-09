import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/MIRIA/Downloads"
to_dir = "C:/Users/MIRIA/Desktop/projeto 103"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Ola, {event.src_path} foi criado!")

    def on_deleted(self, event):
        print(f"Opa! Alguem excluiu {event.src_path} !")

    def on_modified(self, event):
        print(f" {event.smodificourc_path} foi modificado !")

    def on_moved(self, event):
        print(f"{event.src_path} foi movido !")
    
    try:
        while True:
            time.sleep(2)
            print("executando...")
    except KeyboardInterrupt:
        print("interrompido!")
        observer.stop()

 
