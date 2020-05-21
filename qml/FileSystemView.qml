import QtQuick 2.11
import QtQuick.Window 2.2
import QtQuick.Controls 2.2
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Shapes 1.12
import QtQuick.Dialogs 1.0
import QtGraphicalEffects 1.0
import Qt.labs.folderlistmodel 2.14

ListView {
    id: ffListView
    anchors.left: parent.left
    anchors.top: parent.top
    width: parent.width / 4
    height: parent.height * 0.66
    boundsBehavior: Flickable.StopAtBounds
    clip: true
    flickableDirection: Flickable.VerticalFlick
    model: fileModelProvider.model
    delegate: Rectangle {
        id: ffListItem
        width: parent.width
        height: ffListItemText.height + 5
        border.width: 2
        border.color: "black"
        radius: 2
        color: "transparent"
        Text {
            id: ffListItemText
            text: name
            padding: 2
            leftPadding: 15
            font.pointSize: 15
            color: "black"
        }

        MouseArea {
            id: ffListItemMouseArea
            anchors.fill: parent
            hoverEnabled: true
            onEntered: {
                ffListItemText.color = "blue"
                ffListItem.border.color = "blue"
            }

            onExited: {
                ffListItemText.color = "black"
                ffListItem.border.color = "black"
            }

            onClicked: {
                ffListView.model.populate(ffListView.model.getPath(index))
            }
        }
    }

    onCurrentIndexChanged: {

    }
}