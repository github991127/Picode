from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon
from list_themes import *
import Picode


class Stats:
    def __init__(self):
        # 从ui文件中加载UI定义,从UI定义中动态创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了.比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('Picode.ui')
        self.ui.pushButton.clicked.connect(self.handleCalc)
        self.ui.textEdit.returnPressed.connect(self.handleCalc)  # 单行文本框回车消息

    def handleCalc(self):  # ENTER按钮，将输入内容转换为int列表，传给cal计算
        self.ui.textBrowser.clear()
        birthday = self.ui.textEdit.text()
        if not birthday:
            birthday = '31415926'
        outcome = Picode.return_bir(birthday)
        if outcome != -1:
            self.ui.textBrowser.append('{0}出现在圆周率第{1}位'.format(birthday, outcome))
        else:
            self.ui.textBrowser.append('{0}未出现在圆周率前1亿位'.format(birthday))


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('image.png'))
    w = QWidget()
    w.setWindowIcon(QIcon('image.png'))
    apply_stylesheet(app, theme[8], extra=extra, invert_secondary=False)  # 默认False
    stats = Stats()
    stats.ui.show()
    app.exec_()
