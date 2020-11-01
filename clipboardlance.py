#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
#
# Albert Espinoza - 2020
#
import pyperclip
import threading
import time


class ClipboardLance():

    def __init__(self):
        self.stop_monitoring = False
        self.is_run = False
        self.list_update = []

    def start(self) -> str:
        if self.is_run is False:
            print("Thread is Run")
            self.is_run = True
            x = threading.Thread(target=self.monitoring)
            x.start()
        return "Thread is Run"

    def stop_tree(self) -> str:
        self.stop_monitoring = True
        self.is_run = False
        return "Stop thread"

    def monitoring(self) -> list:
        self.stop_monitoring = False
        pyperclip.copy('')
        while self.is_run:
            try:
                clip = pyperclip.paste().encode("utf-8")
                clip = clip.decode("ascii")
            except Exception as e:
                print(e)
                clip = ""

            if (clip not in self.list_update) and (clip != ""):
                print("Add:", clip)
                self.list_update.append(clip)
            if self.stop_monitoring is True:
                # self.save_clipboar_to_file(self.list_update)
                break
            time.sleep(0.5)
        print("Thread is stoped")
        return "Thread is stoped"

    @staticmethod
    def save_clipboar_to_file(lista) -> str:
        with open("detectado.txt", "w") as file:
            file.writelines("\n\n".join(lista[1:]))
        return "Guardado portapapeles en archivo"
