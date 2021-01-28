#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QStyleFactory


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

        menu.addAction(shutdown)
        menu.addAction(exit)

        self.setContextMenu(menu)


def shutdown_func():
    os.system("sudo shutdown now")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tray = Tray()
    tray.show()
    sys.exit(app.exec())
