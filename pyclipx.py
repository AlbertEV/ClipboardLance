#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""Programa que lee el portapapels y guarda los resulatdos en un archivo"""
import pyperclip
import threading
import time


class PyClipX():
    """Main class for pyclipX"""

    def __init__(self):
        print("init PyClipX")
        self.stop_monitoring = False
        self.is_run = False
        self.list_update = [""]

    def start(self):
        """Comprueba que esta corriendo el hilo"""
        if self.is_run is False:
            print("Start Thread")
            self.is_run = True
            x = threading.Thread(target=self.monitoring)
            x.start()
        else:
            print("Thread is Run")

    def monitoring(self):
        """Start monitoring clipboard"""
        self.stop_monitoring = False
        pyperclip.copy('')
        while True:

            try:
                clip = pyperclip.paste().encode("utf-8")
                clip = clip.decode("ascii")
            except Exception as e:
                clip = ""
            if (clip not in self.list_update) and (clip != ""):
                print("Add:", clip)
                self.list_update.append(clip)
            if self.stop_monitoring is True:
                # self.save_clipboar_to_file(self.list_update)
                break
            time.sleep(0.5)
        print("Thread is stoped")

    def stop_tree(self):
        """Stop monitoring clipboard"""
        print("Stoping Thread")
        self.stop_monitoring = True
        self.is_run = False
        # self.list_update = [""]

    @staticmethod
    def save_clipboar_to_file(lista):
        """Save clipboar to file"""
        with open("detectado.txt", "w") as file:
            print("Guardando portapapeles...")
            file.writelines("\n\n".join(lista[1:]))
            print("Guardado.")
