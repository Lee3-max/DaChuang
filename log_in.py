# @Author: Jizheng Lee
# @Time: 2021/8/14
import sys
# QtWidgets中包含的是一些常用控件以及QApplication等Qt界面组件
from typing import Union

try:
    from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
except ImportError:
    from PySide2.QtWidgets import QApplication, QMessageBox
from login_ui import Ui_Form_login

users = {"admin": "huststudent", "LizhengLee": "u202011976"}

#下面的两行设置提示框的提示文件(把经典的Yes,No)换成"好"和"我去修改"
TextStyle ="""
QMessageBox QPushButton[text="&Yes"] {
    qproperty-text: "好";
}
QMessageBox QPushButton[text="&No"] {
    qproperty-text: "我去修改";
}
"""
class MainWin(QWidget, Ui_Form_login):
    def __init__(self):
        super(MainWin, self).__init__()  # 本行内容是一个固定的格式
        self.setupUi(self)  # 本行内容是一个固定的格式

    # 实现槽函数，一般这种函数都需要传入参数self以便于操作ui组件
    def pushBtn_clicked(self):
        """这个函数没啥用，用来测试"""
        print("你点击了登录按钮")

    def User_log(self):
        # 这里输入用户名和密码
        username = self.username_textEdit.toPlainText()
        print(username)
        password = self.password_textEdit.toPlainText()
        print(password)
        if username not in users:
            QMessageBox.information(
                self,'MEssage',"查无此人",
                QMessageBox.Yes, QMessageBox.No
            )
        elif username in users and users.get(username) != password:
            QMessageBox.information(
                self, 'MEssage', "密码错误，请重新输入",
                QMessageBox.Yes, QMessageBox.No
            )

        else:
            print("登陆成功")
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 通过QSS样式的方式设置按钮文字
    app.setStyleSheet(TextStyle)
    myWin = MainWin()
    myWin.show()
    sys.exit(app.exec_())
