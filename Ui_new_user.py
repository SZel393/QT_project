# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_user.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_new_user(object):
    def setupUi(self, new_user):
        new_user.setObjectName("new_user")
        new_user.resize(485, 252)
        self.gridLayout = QtWidgets.QGridLayout(new_user)
        self.gridLayout.setObjectName("gridLayout")
        self.label_password = QtWidgets.QLabel(new_user)
        self.label_password.setObjectName("label_password")
        self.gridLayout.addWidget(self.label_password, 1, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(new_user)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.label_name = QtWidgets.QLabel(new_user)
        self.label_name.setObjectName("label_name")
        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(new_user)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 7, 0, 1, 2)
        self.name = QtWidgets.QLineEdit(new_user)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        self.radioButton_2_4_8 = QtWidgets.QRadioButton(new_user)
        self.radioButton_2_4_8.setObjectName("radioButton_2_4_8")
        self.gridLayout.addWidget(self.radioButton_2_4_8, 3, 0, 1, 2)
        self.radioButton_bin_only = QtWidgets.QRadioButton(new_user)
        self.radioButton_bin_only.setChecked(True)
        self.radioButton_bin_only.setObjectName("radioButton_bin_only")
        self.gridLayout.addWidget(self.radioButton_bin_only, 2, 0, 1, 2)
        self.radioButton_all_syst = QtWidgets.QRadioButton(new_user)
        self.radioButton_all_syst.setObjectName("radioButton_all_syst")
        self.gridLayout.addWidget(self.radioButton_all_syst, 4, 0, 1, 2)
        self.checkBox_droby = QtWidgets.QCheckBox(new_user)
        self.checkBox_droby.setObjectName("checkBox_droby")
        self.gridLayout.addWidget(self.checkBox_droby, 5, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)

        self.retranslateUi(new_user)
        self.buttonBox.accepted.connect(new_user.accept)
        self.buttonBox.rejected.connect(new_user.reject)
        QtCore.QMetaObject.connectSlotsByName(new_user)
        new_user.setTabOrder(self.name, self.password)
        new_user.setTabOrder(self.password, self.radioButton_bin_only)
        new_user.setTabOrder(self.radioButton_bin_only, self.radioButton_2_4_8)
        new_user.setTabOrder(self.radioButton_2_4_8, self.radioButton_all_syst)
        new_user.setTabOrder(self.radioButton_all_syst, self.checkBox_droby)

    def retranslateUi(self, new_user):
        _translate = QtCore.QCoreApplication.translate
        new_user.setWindowTitle(_translate("new_user", "Регистрация нового ученика"))
        self.label_password.setText(_translate("new_user", "Пароль"))
        self.label_name.setText(_translate("new_user", "Имя"))
        self.radioButton_2_4_8.setText(_translate("new_user", "Двоичная, четверичная, восьмеричная системы счисления"))
        self.radioButton_bin_only.setText(_translate("new_user", "Только двоичная система счисления"))
        self.radioButton_all_syst.setText(_translate("new_user", "2-, 4-, 8-, 16-ричные системы счисления"))
        self.checkBox_droby.setText(_translate("new_user", "Использовать дробные числа"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    new_user = QtWidgets.QDialog()
    ui = Ui_new_user()
    ui.setupUi(new_user)
    new_user.show()
    sys.exit(app.exec_())

