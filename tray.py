#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction


class Tray(QSystemTrayIcon):
    def __init__(self):
        super().__init__()

        if os.path.exists("/usr/share/shutdown_tray/icon.png"):
            self.setIcon(QIcon("/usr/share/shutdown_tray/icon.png"))
        elif os.path.exists("icon.png"):
            self.setIcon(QIcon("icon.png"))

        menu = QMenu()

        shutdown = QAction("Shutdown", self)
        shutdown.triggered.connect(shutdown_func)

        exit = QAction("Exit", self)
        exit.triggered.connect(sys.exit)

        suspend = QAction("Suspend", self)
        suspend.triggered.connect(suspend_func)

        reboot = QAction("Reboot", self)
        reboot.triggered.connect(reboot_func)

        lock = QAction("Lock", self)
        lock.triggered.connect(lock_func)

        menu.addAction(shutdown)
        menu.addAction(suspend)
        menu.addAction(reboot)
        menu.addAction(lock)
        menu.addAction(exit)

        self.setContextMenu(menu)


def shutdown_func():
    os.system("sudo systemctl shutdown")


def suspend_func():
    os.system("sudo systemctl suspend")


def reboot_func():
    os.system("sudo systemctl reboot")


def lock_func():
    os.system("i3lock -c 000000")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tray = Tray()
    tray.show()
    sys.exit(app.exec())
