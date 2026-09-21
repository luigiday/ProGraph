from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)

import sys

class Ui_GraphPropDialog(object):
    def setupUi(self, GraphPropDialog):
        if not GraphPropDialog.objectName():
            GraphPropDialog.setObjectName(u"GraphPropDialog")
        GraphPropDialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(GraphPropDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 260, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.lineEdit = QLineEdit(GraphPropDialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 50, 381, 32))
        self.label = QLabel(GraphPropDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 371, 18))
        self.label_2 = QLabel(GraphPropDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 100, 371, 18))
        self.lineEdit_2 = QLineEdit(GraphPropDialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 130, 381, 32))
        self.label_3 = QLabel(GraphPropDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 180, 371, 18))
        self.lineEdit_3 = QLineEdit(GraphPropDialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 210, 381, 32))

        self.retranslateUi(GraphPropDialog)
        self.buttonBox.accepted.connect(GraphPropDialog.accept)
        self.buttonBox.rejected.connect(GraphPropDialog.reject)

        QMetaObject.connectSlotsByName(GraphPropDialog)
    # setupUi

    def retranslateUi(self, GraphPropDialog):
        GraphPropDialog.setWindowTitle(QCoreApplication.translate("GraphPropDialog", u"Propriet\u00e9s du graphique", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("GraphPropDialog", u"Titre", None))
        self.label.setText(QCoreApplication.translate("GraphPropDialog", u"Titre du graphique", None))
        self.label_2.setText(QCoreApplication.translate("GraphPropDialog", u"Titre des abscisses", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("GraphPropDialog", u"X", None))
        self.label_3.setText(QCoreApplication.translate("GraphPropDialog", u"Titre des ordonn\u00e9es", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("GraphPropDialog", u"Y", None))
    # retranslateUi

if __name__ == "__main__": #Fonction aidée par l'IA (les 6 premières lignes)
    app = QApplication(sys.argv)
    dialog = QDialog()
    ui = Ui_GraphPropDialog()
    ui.setupUi(dialog)

    dialog.show()
    sys.exit(app.exec())

