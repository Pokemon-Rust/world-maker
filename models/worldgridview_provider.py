from PySide2 import QtCore
from PIL import Image
import os


class WorldModel(QtCore.QAbstractListModel):
    NameRole = QtCore.Qt.UserRole + 1000
    PathRole = QtCore.Qt.UserRole + 1001
    OffsetX = QtCore.Qt.UserRole + 1002
    OffsetY = QtCore.Qt.UserRole + 1003

    def __init__(self, tiles, parent=None):
        super(WorldModel, self).__init__(parent)
        self._tiles = tiles
        self.width = 0
        self.height = 0

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._tiles)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if 0 <= index.row() < self.rowCount() and index.isValid():
            item = self._tiles[index.row()]
            if role == WorldModel.NameRole:
                return item["name"]
            elif role == WorldModel.PathRole:
                return item["path"]
            elif role == WorldModel.OffsetX:
                return item["offsetx"]
            elif role == WorldModel.OffsetY:
                return item["offsety"]

    def roleNames(self):
        roles = {WorldModel.NameRole: b"name", WorldModel.PathRole: b"path", WorldModel.OffsetX: b"offsetx",
                 WorldModel.OffsetY: b"offsety"}
        return roles

    def appendRow(self, row):
        self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(), self.rowCount())
        self._tiles.append(row)
        self.endInsertRows()

    def reset(self, new_tiles):
        self.beginResetModel()
        self._tiles = new_tiles
        self.endResetModel()

    @QtCore.Slot(int, result=str)
    def getName(self, index):
        if index not in range(0, self.rowCount()):
            return ''
        return self._tiles[index]['name']

    @QtCore.Slot(int, result=str)
    def getPath(self, index):
        if index not in range(0, self.rowCount()):
            return ''
        return self._tiles[index]['path']

    @QtCore.Slot(int, result=int)
    def getOffsetX(self, index):
        if index not in range(0, self.rowCount()):
            return ''
        return self._tiles[index]['offsetx']

    @QtCore.Slot(int, result=int)
    def getOffsetY(self, index):
        if index not in range(0, self.rowCount()):
            return ''
        return self._tiles[index]['offsety']

    @QtCore.Slot(int, int)
    def populate(self, width, height):
        new_tiles = []
        self.width = width
        self.height = height
        for i in range(width * height):
            new_tiles.append({
                "name": "null",
                "path": os.path.abspath("res/blank_image.png"),
                "offsetx": 0,
                "offsety": 0
            })

        self.reset(new_tiles)

    @QtCore.Slot(int, str, result=bool)
    def placeImage(self, index, path):
        image = Image.open(path)
        image_width, image_height = image.size


class WorldModelProvider(QtCore.QObject):
    def __init__(self, files, parent=None):
        super(WorldModelProvider, self).__init__(parent)
        self._model = WorldModel(files)

    @QtCore.Property(QtCore.QObject, constant=True)
    def model(self):
        return self._model
