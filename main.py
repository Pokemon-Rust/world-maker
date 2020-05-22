import sys
import os
from PySide2 import QtCore, QtGui, QtQuick, QtQml

from models.backend import Backend

backend = Backend()

def qt_bind(engine):
    directory = os.path.dirname(os.path.abspath(__file__))
    engine.rootContext().setContextProperty("backend", backend)
    engine.load(QtCore.QUrl.fromLocalFile(os.path.join(directory, 'qml/MainWindow.qml')))
    if not engine.rootObjects():
        print("Error while enumerating root objects..")


if __name__ == '__main__':
    app = QtGui.QGuiApplication(sys.argv)
    engine = QtQml.QQmlApplicationEngine()
    qt_bind(engine)
    app.exec_()
