import sys
from my_timer import *
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore
from pydub import AudioSegment
from pydub.playback import play
from PySide6.QtCore import QThread, Signal


class CloneThread(QThread):
    signal = Signal('PyQt_PyObject')
    def __init__(self):
        QThread.__init__(self)
    def run(self):
        music = AudioSegment.from_mp3(
            "C:\\Users\\tuhin Mitra\\Desktop\\All Python Resources\\gui_project\\alarm.mp3")  # path to the audio file that will play after time is over
        play(music)
        self.signal.emit('')  # signal for main thread to understand this thread working has finished!
class Mytimer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.thread1 = CloneThread()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()
        self.curr_time = QtCore.QTime(0, 0, 0) # initialize to 0
        self.Reach_timer = self.curr_time
        self.thread1.signal.connect(self.thread1.terminate)
        self.time = QtCore.QTime(self.curr_time)
        self.timer.timeout.connect(self.TimerEvent)
        self.ui.pushButton.clicked.connect(self.terminal)  # action for push button click
    def TimerEvent(self):
        self.time = self.time.addSecs(1)  # add seconds to running time
        if self.time.toString() == self.Reach_timer.toString():  # check if destination is reached
            print('Time Reached')
            self.timer.stop()
            self.thread1.start()
            self.thread1.start()
        self.ui.label.setText(self.time.toString("hh:mm:ss"))  # to display the count
    def terminal(self):
        button_text = self.ui.pushButton.text()
        if button_text == 'START':
            # self.ui.pushButton.setDisabled(True)
            minutes = int(self.ui.spinBox.text())  # get text from spin box
            self.set_timer = minutes * 60  # converted into seconds
            self.Reach_timer = self.curr_time.addSecs(minutes * 60)  # set the destination
            self.ui.pushButton.setText('STOP')  # set button text for stop
            self.timer.start(1000)  # start timer, after every 1000 ms it will call TimerEvent to increase the counting
        else:
            self.thread1.terminate()  # this will terminate the playing of the audio file
            self.curr_time = QtCore.QTime(0, 0, 0)
            self.time = self.curr_time  # re-initialize to 0
            self.ui.pushButton.setText('START')  # show push button text as "start"
            self.timer.stop()  # when stop is pressed, stop the timer
if 1 == 1:
    app = QApplication(sys.argv)
    w = Mytimer()
    w.show()
    sys.exit(app.exec())