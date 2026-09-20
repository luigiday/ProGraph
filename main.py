
try:
    from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
        QMetaObject, QObject, QPoint, QRect,
        QSize, QTime, QUrl, Qt, QStringListModel)
    from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
        QCursor, QFont, QFontDatabase, QGradient,
        QIcon, QImage, QKeySequence, QLinearGradient,
        QPainter, QPalette, QPixmap, QRadialGradient,
        QTransform)
    from PySide6.QtWidgets import (QApplication, QDockWidget, QHeaderView, QLineEdit,
        QListView, QMainWindow, QMenu, QMenuBar,
        QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
        QToolBar, QVBoxLayout, QWidget, QMessageBox)
except ModuleNotFoundError:
    print('''FATAL :
    Les modules ne sont pas installé !
    Veuillez éxecuter la commande : 
    Windows : pip install PySide6
    Linux (fedora) : sudo dnf install python3-pyside6 (autres distribs, voir "Installer PySide6 dans votre gestionnaire de paquets")''')
import sys
from calculator import calculate


def show_app_error(parent, message):
    print(f'''Dump de l'erreur d'app\n\n{message}\n\nFin du dump''')
    QMessageBox.critical(parent, "Une erreur est survenue dans l'application", message)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(958, 600)
        self.actionA_propos = QAction(MainWindow)
        self.actionA_propos.setObjectName(u"actionA_propos")
        self.actionCharger_des_valeurs = QAction(MainWindow)
        self.actionCharger_des_valeurs.setObjectName(u"actionCharger_des_valeurs")
        self.actionExporter_des_valeurs = QAction(MainWindow)
        self.actionExporter_des_valeurs.setObjectName(u"actionExporter_des_valeurs")
        self.actionEffacer_toutes_les_valeurs = QAction(MainWindow)
        self.actionEffacer_toutes_les_valeurs.setObjectName(u"actionEffacer_toutes_les_valeurs")
        self.actionOuvrir = QAction(MainWindow)
        self.actionOuvrir.setObjectName(u"actionOuvrir")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.actionOuvrir.setIcon(icon)
        self.actionEnregistrer = QAction(MainWindow)
        self.actionEnregistrer.setObjectName(u"actionEnregistrer")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderOpen))
        self.actionEnregistrer.setIcon(icon1)
        self.actionEnregistrer_sous = QAction(MainWindow)
        self.actionEnregistrer_sous.setObjectName(u"actionEnregistrer_sous")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InputKeyboard))
        self.actionEnregistrer_sous.setIcon(icon2)
        self.actionOuvrirtoolbar = QAction(MainWindow)
        self.actionOuvrirtoolbar.setObjectName(u"actionOuvrirtoolbar")
        self.actionOuvrirtoolbar.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 958, 30))
        self.menuFichier = QMenu(self.menubar)
        self.menuFichier.setObjectName(u"menuFichier")
        self.menu_dition = QMenu(self.menubar)
        self.menu_dition.setObjectName(u"menu_dition")
        self.menuGraphe = QMenu(self.menubar)
        self.menuGraphe.setObjectName(u"menuGraphe")
        self.menuTableau = QMenu(self.menubar)
        self.menuTableau.setObjectName(u"menuTableau")
        self.menuAide = QMenu(self.menubar)
        self.menuAide.setObjectName(u"menuAide")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.dockWidgetContents)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockWidget)
        self.dockWidget_2 = QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listView = QListView(self.dockWidgetContents_2)
        self.listView.setObjectName(u"listView")
        self.listView.setFlow(QListView.Flow.TopToBottom)

        self.verticalLayout_2.addWidget(self.listView)

        self.lineEdit = QLineEdit(self.dockWidgetContents_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockWidget_2)
        self.maintoolBar = QToolBar(MainWindow)
        self.maintoolBar.setObjectName(u"maintoolBar")
        self.maintoolBar.setMovable(False)
        self.maintoolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.maintoolBar)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menu_dition.menuAction())
        self.menubar.addAction(self.menuGraphe.menuAction())
        self.menubar.addAction(self.menuTableau.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionEnregistrer)
        self.menuFichier.addAction(self.actionEnregistrer_sous)
        self.menuTableau.addAction(self.actionCharger_des_valeurs)
        self.menuTableau.addAction(self.actionExporter_des_valeurs)
        self.menuTableau.addAction(self.actionEffacer_toutes_les_valeurs)
        self.menuAide.addAction(self.actionA_propos)
        self.maintoolBar.addAction(self.actionOuvrir)
        self.maintoolBar.addAction(self.actionEnregistrer)
        self.maintoolBar.addAction(self.actionEnregistrer_sous)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ProGraph", None))
        self.actionA_propos.setText(QCoreApplication.translate("MainWindow", u"A propos", None))
        self.actionCharger_des_valeurs.setText(QCoreApplication.translate("MainWindow", u"Charger des valeurs", None))
        self.actionExporter_des_valeurs.setText(QCoreApplication.translate("MainWindow", u"Exporter des valeurs", None))
        self.actionEffacer_toutes_les_valeurs.setText(QCoreApplication.translate("MainWindow", u"Effacer toutes les valeurs", None))
        self.actionOuvrir.setText(QCoreApplication.translate("MainWindow", u"Nouveau", None))
        self.actionEnregistrer.setText(QCoreApplication.translate("MainWindow", u"Ouvrir", None))
        self.actionEnregistrer_sous.setText(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.actionOuvrirtoolbar.setText(QCoreApplication.translate("MainWindow", u"Ouvrir", None))
#if QT_CONFIG(tooltip)
        self.actionOuvrirtoolbar.setToolTip(QCoreApplication.translate("MainWindow", u"Ouvre un fichier", None))
#endif // QT_CONFIG(tooltip)
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"Fichier", None))
        self.menu_dition.setTitle(QCoreApplication.translate("MainWindow", u"\u00c9dition", None))
        self.menuGraphe.setTitle(QCoreApplication.translate("MainWindow", u"Graphe", None))
        self.menuTableau.setTitle(QCoreApplication.translate("MainWindow", u"Tableau", None))
        self.menuAide.setTitle(QCoreApplication.translate("MainWindow", u"Aide", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tableau de valeurs", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"X", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.dockWidget_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculatrice", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Saisir une expression", None))
        self.maintoolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"Barre d'outils principale", None))
    # retranslateUi

    def show_info_simple(self, text):
        try:
            msgBox = QMessageBox(parent=main_window)
            msgBox.setText(f"{text}")
            msgBox.setInformativeText(f"Message : {text}")
            msgBox.setIcon(QMessageBox.Icon.Information)
            msgBox.setWindowTitle("Information - ProGraph")
            msgBox.exec()
        except Exception as e:
            show_app_error(main_window, f'''Impossible d'afficher l'alerte "info_simple"\nMessage : {e}''')

    def show_error_simple(self, action, text):
        try:
            msgBox = QMessageBox(parent=main_window)
            msgBox.setText(f"Une erreur est survenue dans l'action \"{action}\"")
            msgBox.setInformativeText(f"Message : {text}")
            msgBox.setIcon(QMessageBox.Icon.Warning)
            msgBox.setWindowTitle("Erreur de sous-module (non-fatale)")
            msgBox.exec()
        except Exception as e:
            show_app_error(main_window, f'''Impossible d'afficher l'alerte "error_simple"\nMessage : {e}''')

    def calculator(self, MainWindow):
        pass


if __name__ == "__main__": #Fonction aidée par l'IA (les 6 premières lignes)
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)

    results_model = QStringListModel()
    ui.listView.setModel(results_model)

    def handle_expression(): # Gère la saisie dans la calculatrice
        expression = ui.lineEdit.text() # On récupere le texte du champ
        if expression.strip(): # on verifie que le champ n'est pas vide
            try:
                result = calculate(expression) # On utilise la fonction de la classe calulator pour obtenir un résultat
                results = results_model.stringList()
                results.append(f"{expression} = {result}") # On formatte ca joliment
                results_model.setStringList(results) # On ajoute a la liste
            except Exception as e:
                ui.show_error_simple("calcul", str(e))
        ui.lineEdit.clear() # On efface le champ de saisie

    ui.lineEdit.returnPressed.connect(handle_expression) # Demande a champ de saisie de nous dire quand l'utilisateur appuie sur entrée
    main_window.show()
    sys.exit(app.exec())

