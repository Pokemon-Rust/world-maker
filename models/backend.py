from PySide2 import QtQuick, QtCore, QtGui, QtQml
import os

from models.filesystem_model import FileModelProvider
from models.imagegridview_model import ImageModelProvider


class Backend(QtCore.QObject):
    def __init__(self, parent=None):
        super(Backend, self).__init__(parent)
        self._imageModelProvider = ImageModelProvider([])
        self._fileModelProvider = FileModelProvider([{"name": "/", "path": "/"}], self.populateImageModel)

    def populateImageModel(self, dir):
        self._imageModelProvider.model.populate(dir)

    @QtCore.Property(QtCore.QObject, constant=True)
    def fileModelProvider(self):
        return self._fileModelProvider

    @QtCore.Property(QtCore.QObject, constant=True)
    def imageModelProvider(self):
        return self._imageModelProvider