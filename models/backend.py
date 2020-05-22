from PySide2 import QtCore

from models.filesystem_model import FileModelProvider
from models.imagegridview_model import ImageModelProvider
from models.worldgridview_provider import WorldModelProvider


class Backend(QtCore.QObject):
    def __init__(self, parent=None):
        super(Backend, self).__init__(parent)
        self._imageModelProvider = ImageModelProvider([])
        self._fileModelProvider = FileModelProvider([{"name": "/", "path": "/"}], self.populateImageModel)
        self._worldModelProvider = WorldModelProvider([])

    def populateImageModel(self, dir):
        self._imageModelProvider.model.populate(dir)

    @QtCore.Property(QtCore.QObject, constant=True)
    def fileModelProvider(self):
        return self._fileModelProvider

    @QtCore.Property(QtCore.QObject, constant=True)
    def imageModelProvider(self):
        return self._imageModelProvider

    @QtCore.Property(QtCore.QObject, constant=True)
    def worldModelProvider(self):
        return self._worldModelProvider

    @QtCore.Property(int, constant=True)
    def numHorCell(self):
        return 50

    @QtCore.Property(int, constant=True)
    def numVerCell(self):
        return 50