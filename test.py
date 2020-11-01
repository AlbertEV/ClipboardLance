import clipboardlance
import pytest
from time import sleep
import pyperclip
import random


def test_class_var_init():
    app = clipboardlance.ClipboardLance()
    assert app.stop_monitoring is False
    assert app.is_run is False
    assert app.list_update == []


def test_stop():
    app = clipboardlance.ClipboardLance()
    assert app.stop_tree() == "Stop thread"
    assert app.is_run is False
    assert app.stop_monitoring is True


def test_monitorin_not_start_alone():
    app = clipboardlance.ClipboardLance()
    assert app.monitoring() == "Thread is stoped"


def test_star_and_stop_monitoring():
    app = clipboardlance.ClipboardLance()
    assert app.is_run is False
    app.start()
    assert app.is_run is True, app.stop_tree()
    sleep(1)
    app.stop_tree()
    assert app.is_run is False, app.stop_tree()


def test_copy_from_clipboard():
    app = clipboardlance.ClipboardLance()
    app.start()
    sleep(1)
    paste_clip = 'test con pytest'
    pyperclip.copy(paste_clip)
    sleep(1)
    assert paste_clip in app.list_update, app.stop_tree()
    app.stop_tree()


def test_multi_copy_from_clipboard():
    app = clipboardlance.ClipboardLance()
    app.start()
    sleep(1)
    clipboard_list_test = ["test", "con", "pytest", "es", "rapido"]
    for i in clipboard_list_test:
        pyperclip.copy(i)
        sleep(0.5)
    paste_clip = random.choice(clipboard_list_test)
    assert paste_clip in app.list_update, app.stop_tree()
    assert len(clipboard_list_test) == len(app.list_update), app.stop_tree()
    app.stop_tree()
