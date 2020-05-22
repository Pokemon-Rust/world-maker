import QtQuick 2.11
import QtQuick.Window 2.2
import QtQuick.Controls 2.2
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.3
import QtQuick.Shapes 1.12
import QtQuick.Dialogs 1.0
import QtGraphicalEffects 1.0

Rectangle {
    width: parent.width * 0.7
    height: parent.height * 0.66
    anchors.left: fileSystemView.right
    anchors.top: parent.top
    border.width: 2
    border.color: "black"
    color: "transparent"

    Component {
        id: worldItemDelegate
        Rectangle {
            id: gridItem
            width: grid.cellWidth
            height: grid.cellHeight - 1
            border.width: 0.5
            border.color: "black"
            color: "transparent"
            clip: true
            Column {
                anchors.fill: parent
                clip: true
                Image {
                    source: path
                    x: gridItem.border.width + offsetx
                    y: gridItem.border.width + offsety
                    width: grid.cellWidth
                    height: grid.cellHeight
                    fillMode: Image.Pad

                }
            }

            MouseArea {
                id: gridItemMouseArea
                anchors.fill: parent
                hoverEnabled: true
                onEntered: {
                    gridItem.color = "blue"
                }

                onExited: {
                    gridItem.color = "transparent"
                    gridItem.border.color = "black"
                }

            }


        }
    }

    ScrollView {
        id: worldLayerScrollView
        clip: true
        anchors.left: parent.left
        anchors.top: parent.top
        height: parent.height
        width: parent.width


        Flickable {
            id: worldLayerFlickable

            width: backend.numHorCell * grid.cellWidth
            height: backend.numVerCell * grid.cellHeight

            contentHeight: backend.numVerCell * grid.cellHeight
            contentWidth: backend.numHorCell * grid.cellWidth
            boundsBehavior: Flickable.StopAtBounds

            GridView {
                id: grid
                anchors.fill: parent

                cellWidth: 64; cellHeight: 64

                width: backend.numHorCell * cellWidth
                height: backend.numVerCell * cellHeight

                boundsBehavior: Flickable.StopAtBounds
                clip: true
                flickableDirection: Flickable.VerticalFlick
                model: backend.worldModelProvider.model
                delegate: worldItemDelegate
                focus: true

                Component.onCompleted: {
                    model.populate(backend.numHorCell, backend.numVerCell)
                }
            }
        }
    }
}

