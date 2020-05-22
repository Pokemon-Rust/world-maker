from PySide2 import QtCore
import os


class ImageModel(QtCore.QAbstractListModel):
    NameRole = QtCore.Qt.UserRole + 1000
    PathRole = QtCore.Qt.UserRole + 1001

    def __init__(self, files, parent=None):
        super(ImageModel, self).__init__(parent)
        self._files = files

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._files)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if 0 <= index.row() < self.rowCount() and index.isValid():
            item = self._files[index.row()]
            if role == ImageModel.NameRole:
                return item["name"]
            elif role == ImageModel.PathRole:
                return item["path"]

    def roleNames(self):
        roles = {ImageModel.NameRole: b"name", ImageModel.PathRole: b"path"}
        return roles

    def appendRow(self, row):
        self.beginInsertRows(QtCore.QModelIndex(), self.rowCount(), self.rowCount())
        self._files.append(row)
        self.endInsertRows()

    def reset(self, new_files):
        self.beginResetModel()
        self._files = new_files
        self.endResetModel()

    @QtCore.Slot(int, result=str)
    def getName(self, index):
        if index not in range(0, self.rowCount()):
            return ''
        return self._files[index]['name']

    @QtCore.Slot(int, result=str)
    def getPath(self, index):
        if index not in range(0, self.rowCount()):
            return ''
        return self._files[index]['path']

    @QtCore.Slot(str)
    def populate(self, dir):
        entries = os.listdir(dir)
        new_files = []
        for entry in entries:
            if os.path.isfile(dir + os.sep + entry) and entry.endswith(".png"):
                new_files.append({"name": entry, "path": dir + os.sep + entry})
        new_files = sorted(new_files, key=lambda x: x["name"])
        self.reset(new_files)


class ImageModelProvider(QtCore.QObject):
    def __init__(self, files, parent=None):
        super(ImageModelProvider, self).__init__(parent)
        self._model = ImageModel(files)

    @QtCore.Property(QtCore.QObject, constant=True)
    def model(self):
        return self._model
