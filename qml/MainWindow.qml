import QtQuick 2.11
import QtQuick.Window 2.2
import QtQuick.Controls 2.2
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Shapes 1.12
import QtQuick.Dialogs 1.0
import QtGraphicalEffects 1.0

ApplicationWindow {
    id: window
    visible: true
    width: 960
    height: 960
    visibility: "Maximized"

    minimumHeight: 480
    minimumWidth: 640
    title: "World-Maker"

    color: "white"

    Rectangle {
        id: toolBar
        width: parent.width
        height: 64
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
    }

    Rectangle {
        id: views
        color: "transparent"
        width: parent.width
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        anchors.top: toolBar.bottom

        FileSystemView {
            id: fileSystemView
        }

        ImageGridView {}

        WorldGridView {}
    }


}
