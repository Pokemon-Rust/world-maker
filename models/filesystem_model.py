from PySide2 import QtQuick, QtCore, QtGui, QtQml
import os


class FileModel(QtCore.QAbstractListModel):
    NameRole = QtCore.Qt.UserRole + 1000
    PathRole = QtCore.Qt.UserRole + 1001

    def __init__(self, files, parent=None):
        super(FileModel, self).__init__(parent)
        self._files = files

    def rowCount(self, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return 0
        return len(self._files)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if 0 <= index.row() < self.rowCount() and index.isValid():
            item = self._files[index.row()]
            if role == FileModel.NameRole:
                return item["name"]
            elif role == FileModel.PathRole:
                return item["path"]

    def roleNames(self):
        roles = {}
        roles[FileModel.NameRole] = b"name"
        roles[FileModel.PathRole] = b"path"
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
        new_files = [{"name": "..", "path": dir + os.sep + ".."}]
        for entry in entries:
            if os.path.isdir(dir + os.sep + entry):
                new_files.append({"name": entry, "path": dir + os.sep + entry})

        self.reset(new_files)


class FileModelProvider(QtCore.QObject):
    def __init__(self, files, parent=None):
        super(FileModelProvider, self).__init__(parent)
        self._model = FileModel(files)

    @QtCore.Property(QtCore.QObject, constant=True)
    def model(self):
        return self._model
