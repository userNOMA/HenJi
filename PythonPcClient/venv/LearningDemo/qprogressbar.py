import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar,
                             QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 创建一个进度条
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        # 创建一个按钮
        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        # 将按钮关联到soAction函数
        self.btn.clicked.connect(self.doAction)

        # 创建一个计时器
        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    # 重写计时器
    def timerEvent(self, e):

        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        # 进度条上显示计时器模拟进度
        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            # 启动计时器
            self.timer.start(100, self)
            self.btn.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())