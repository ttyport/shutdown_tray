#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from sys import argv, exit
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QStyleFactory


class Tray(QSystemTrayIcon):
    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("/usr/share/shutdown_tray/icon.png"))
        menu = QMenu()
        shutdown = QAction("Shutdown", self)
        shutdown.triggered.connect(shutdown_func)
        menu.addAction(shutdown)
        self.setContextMenu(menu)


def shutdown_func():
    os.system("shutdown now")


if __name__ == '__main__':
    app = QApplication(argv)
    tray = Tray()
    tray.show()
    exit(app.exec())
