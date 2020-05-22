import QtQuick 2.11
import QtQuick.Window 2.2
import QtQuick.Controls 2.2
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Shapes 1.12
import QtQuick.Dialogs 1.0
import QtGraphicalEffects 1.0

Rectangle {
    width: parent.width * 0.75
    height: parent.height * 0.33
    anchors.left: parent.left
    anchors.bottom: parent.bottom
    border.width: 2
    border.color: "black"
    color: "transparent"
    
    Component {
        id: imageItemDelegate
        Rectangle {
            id: gridItem
            width: grid.cellWidth
            height: grid.cellHeight - 4
            border.width: 2
            border.color: "black"
            color: "black"
            Column {
                anchors.fill: parent
                Image {
                    source: path
                    anchors.horizontalCenter: parent.horizontalCenter
                    y: gridItem.border.width
                    width: grid.cellWidth - 2 * gridItem.border.width
                    height: grid.cellHeight - gridItemText.height - 2 * gridItem.border.width
                }
                Text {
                    id: gridItemText
                    text: name
                    color: "white"
                    leftPadding: 5
                    bottomPadding: 10
                    wrapMode: Text.WordWrap
                    width: grid.cellWidth - 2 * gridItem.border.width
                    height: 20

                    anchors.horizontalCenter: parent.horizontalCenter
                }
            }

            MouseArea {
                id: gridItemMouseArea
                anchors.fill: parent
                hoverEnabled: true
                onEntered: {
                    gridItem.border.color = "blue"
                    gridItem.color = "blue"
                }

                onExited: {
                    gridItem.border.color = "black"
                    gridItem.color = "black"
                }

            }


        }
    }
    
    GridView {
        id: grid
        anchors.fill: parent
        cellWidth: 128; cellHeight: 128
        boundsBehavior: Flickable.StopAtBounds
        clip: true
        flickableDirection: Flickable.VerticalFlick
        model: backend.imageModelProvider.model
        delegate: imageItemDelegate
        highlight: Rectangle { color: "lightsteelblue"; radius: 5 }
        focus: true
    }
}
