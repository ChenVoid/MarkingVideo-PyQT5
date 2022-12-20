import os

import PyQt5
from PyQt5.QtCore import pyqtSignal, QDateTime
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog

from config import usrConfig
from utils import store, load
from utils.myVideoWidget import myVideoWidget
from view.forms.MarkingVideo import Ui_MainWindow


class MarkingVideoSlot(QMainWindow, Ui_MainWindow):

    # show_signal = pyqtSignal(list, int, int)
    # new_start = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(MarkingVideoSlot, self).__init__(parent)
        self.setupUi(self)

        # 初始化变量
        # videoList列表，记录video文件夹目录下的所有文件名str
        self.videoList = []
        # log列表，记录一组32道题答案
        self.log = []
        self.ansList = []
        self.video_name = "questions"
        self.videoPath = ""
        self.videoIndex = 1
        # ans是列表，元素是log
        self.ans = []
        self.ifImportVideoFirst = 0

        # 点击事件
        # self.show_signal.connect(self.show_slot)
        # self.pushButton_ok.clicked.connect(self.store)
        self.btn_next.clicked.connect(self.next)
        self.btn_questions.clicked.connect(self.importQue)
        self.btn_save.clicked.connect(self.saveAns)

        self.sld_video_pressed = False  # 判断当前进度条识别否被鼠标点击
        self.videoFullScreen = False  # 判断当前widget是否全屏
        self.videoFullScreenWidget = myVideoWidget()  # 创建一个全屏的widget
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video)  # 视频播放输出的widget，就是上面定义的
        self.btn_open.clicked.connect(self.openVideoFile)  # 打开视频文件按钮
        self.btn_play.clicked.connect(self.playVideo)  # play
        self.btn_stop.clicked.connect(self.pauseVideo)  # pause
        # self.btn_cast.clicked.connect(self.castVideo)  # 视频截图
        self.player.positionChanged.connect(self.changeSlide)  # change Slide
        self.videoFullScreenWidget.doubleClickedItem.connect(self.videoDoubleClicked)  # 双击响应
        self.wgt_video.doubleClickedItem.connect(self.videoDoubleClicked)  # 双击响应
        self.sld_video.setTracking(False)
        self.sld_video.sliderReleased.connect(self.releaseSlider)
        self.sld_video.sliderPressed.connect(self.pressSlider)
        self.sld_video.sliderMoved.connect(self.moveSlider)  # 进度条拖拽跳转
        self.sld_video.ClickedValue.connect(self.clickedSlider)  # 进度条点击跳转
        self.sld_audio.valueChanged.connect(self.volumeChange)  # 控制声音播放
        # self.btn_cast.hide()

        # 初始化
        # self.init()

    def init(self):
        # VideoPath是写在usrConfig中的路径：VideoPath = "./video"，其中存储了视频
        # os.listdir(path)返回path目录下所有文件或文件夹的名字的列表，VideoList是str的列表
        # self.videoList = os.listdir(usrConfig.VideoPath)

        print(self.videoList)
        # print("yes")

    def store_log(self):
        self.log.append("video" + str(self.videoIndex))
        self.log.append(self.lineEdit_001.text())
        self.log.append(self.lineEdit_002.text())
        self.log.append(self.lineEdit_003.text())
        self.log.append(self.lineEdit_004.text())
        self.log.append(self.lineEdit_005.text())
        self.log.append(self.lineEdit_006.text())
        self.log.append(self.lineEdit_007.text())
        self.log.append(self.lineEdit_008.text())
        self.log.append(self.lineEdit_009.text())
        self.log.append(self.lineEdit_010.text())
        self.log.append(self.lineEdit_011.text())
        self.log.append(self.lineEdit_012.text())
        self.log.append(self.lineEdit_013.text())
        self.log.append(self.lineEdit_014.text())
        self.log.append(self.lineEdit_015.text())
        self.log.append(self.lineEdit_016.text())
        self.log.append(self.lineEdit_017.text())
        self.log.append(self.lineEdit_018.text())
        self.log.append(self.lineEdit_019.text())
        self.log.append(self.lineEdit_020.text())
        self.log.append(self.lineEdit_021.text())
        self.log.append(self.lineEdit_022.text())
        self.log.append(self.lineEdit_023.text())
        self.log.append(self.lineEdit_024.text())
        self.log.append(self.lineEdit_025.text())
        self.log.append(self.lineEdit_026.text())
        self.log.append(self.lineEdit_027.text())
        self.log.append(self.lineEdit_028.text())
        self.log.append(self.lineEdit_029.text())
        self.log.append(self.lineEdit_030.text())
        self.log.append(self.lineEdit_031.text())
        self.log.append(self.lineEdit_032.text())

    def clearAns(self):
        self.lineEdit_001.setText("")
        self.lineEdit_002.setText("")
        self.lineEdit_003.setText("")
        self.lineEdit_004.setText("")
        self.lineEdit_005.setText("")
        self.lineEdit_006.setText("")
        self.lineEdit_007.setText("")
        self.lineEdit_008.setText("")
        self.lineEdit_009.setText("")
        self.lineEdit_010.setText("")
        self.lineEdit_011.setText("")
        self.lineEdit_012.setText("")
        self.lineEdit_013.setText("")
        self.lineEdit_014.setText("")
        self.lineEdit_015.setText("")
        self.lineEdit_016.setText("")
        self.lineEdit_017.setText("")
        self.lineEdit_018.setText("")
        self.lineEdit_019.setText("")
        self.lineEdit_020.setText("")
        self.lineEdit_021.setText("")
        self.lineEdit_022.setText("")
        self.lineEdit_023.setText("")
        self.lineEdit_024.setText("")
        self.lineEdit_025.setText("")
        self.lineEdit_026.setText("")
        self.lineEdit_027.setText("")
        self.lineEdit_028.setText("")
        self.lineEdit_029.setText("")
        self.lineEdit_030.setText("")
        self.lineEdit_031.setText("")
        self.lineEdit_032.setText("")

    def ifFinished(self):
        if self.lineEdit_001.text() and self.lineEdit_002.text() and self.lineEdit_003.text() and self.lineEdit_004.text() and self.lineEdit_005.text() and self.lineEdit_006.text() and self.lineEdit_007.text() and self.lineEdit_008.text() and self.lineEdit_009.text() and self.lineEdit_010.text() and self.lineEdit_011.text() and self.lineEdit_012.text() and self.lineEdit_013.text() and self.lineEdit_014.text() and self.lineEdit_015.text() and self.lineEdit_016.text() and self.lineEdit_017.text() and self.lineEdit_018.text() and self.lineEdit_019.text() and self.lineEdit_020.text() and self.lineEdit_021.text() and self.lineEdit_022.text() and self.lineEdit_023.text() and self.lineEdit_024.text() and self.lineEdit_025.text() and self.lineEdit_026.text() and self.lineEdit_027.text() and self.lineEdit_028.text() and self.lineEdit_029.text() and self.lineEdit_030.text() and self.lineEdit_031.text() and self.lineEdit_032.text() :
            return True
        else:
            return False

    def load(self):
        # reader是元组，reader[0]是列表，reader[0][0]是str
        flag, reader = load.load_que(self.video_name)
        # print(reader[0][0])
        if flag:
            self.textBrowser_001.setText(reader[0][0])
            self.textBrowser_002.setText(reader[1][0])
            self.textBrowser_003.setText(reader[2][0])
            self.textBrowser_004.setText(reader[3][0])
            self.textBrowser_005.setText(reader[4][0])
            self.textBrowser_006.setText(reader[5][0])
            self.textBrowser_007.setText(reader[6][0])
            self.textBrowser_008.setText(reader[7][0])
            self.textBrowser_009.setText(reader[8][0])
            self.textBrowser_010.setText(reader[9][0])
            self.textBrowser_011.setText(reader[10][0])
            self.textBrowser_012.setText(reader[11][0])
            self.textBrowser_013.setText(reader[12][0])
            self.textBrowser_014.setText(reader[13][0])
            self.textBrowser_015.setText(reader[14][0])
            self.textBrowser_016.setText(reader[15][0])
            self.textBrowser_017.setText(reader[16][0])
            self.textBrowser_018.setText(reader[17][0])
            self.textBrowser_019.setText(reader[18][0])
            self.textBrowser_020.setText(reader[19][0])
            self.textBrowser_021.setText(reader[20][0])
            self.textBrowser_022.setText(reader[21][0])
            self.textBrowser_023.setText(reader[22][0])
            self.textBrowser_024.setText(reader[23][0])
            self.textBrowser_025.setText(reader[24][0])
            self.textBrowser_026.setText(reader[25][0])
            self.textBrowser_027.setText(reader[26][0])
            self.textBrowser_028.setText(reader[27][0])
            self.textBrowser_029.setText(reader[28][0])
            self.textBrowser_030.setText(reader[29][0])
            self.textBrowser_031.setText(reader[30][0])
            self.textBrowser_032.setText(reader[31][0])
            QMessageBox.information(self, "Success!", "题目已导入！")
        else:
            self.player.pause()
            QMessageBox.information(self, "Error!", "未找到题目！")
            # self.player.pause()

    '''
        def castVideo(self):
        screen = QGuiApplication.primaryScreen()
        cast_jpg = './' + QDateTime.currentDateTime().toString("yyyy-MM-dd hh-mm-ss-zzz") + '.jpg'
        screen.grabWindow(self.wgt_video.winId()).save(cast_jpg)
    '''

    def volumeChange(self, position):
        volume = round(position / self.sld_audio.maximum() * 100)
        print("vlume %f" % volume)
        self.player.setVolume(volume)
        self.lab_audio.setText("volume:" + str(volume) + "%")

    def clickedSlider(self, position):
        if self.player.duration() > 0:  # 开始播放后才允许进行跳转
            video_position = int((position / 100) * self.player.duration())
            self.player.setPosition(video_position)
            self.lab_video.setText("%.2f%%" % position)
        else:
            self.sld_video.setValue(0)

    def moveSlider(self, position):
        self.sld_video_pressed = True
        if self.player.duration() > 0:  # 开始播放后才允许进行跳转
            video_position = int((position / 100) * self.player.duration())
            self.player.setPosition(video_position)
            self.lab_video.setText("%.2f%%" % position)

    def pressSlider(self):
        self.sld_video_pressed = True
        print("pressed")

    def releaseSlider(self):
        self.sld_video_pressed = False

    def changeSlide(self, position):
        if not self.sld_video_pressed:  # 进度条被鼠标点击时不更新
            self.vidoeLength = self.player.duration() + 0.1
            self.sld_video.setValue(round((position / self.vidoeLength) * 100))
            self.lab_video.setText("%.2f%%" % ((position / self.vidoeLength) * 100))

    def openVideoFile(self):
        if self.ifImportVideoFirst == 0:
            self.videoList = os.listdir(usrConfig.VideoBasePath)
            if self.videoList:
                self.videoPath = usrConfig.VideoBasePath + '/' + self.videoList[0]

                OpenVideoUrl = PyQt5.QtCore.QUrl(self.videoPath)
                # OpenFileUrl = QFileDialog.getOpenFileUrl()[0]
                print(type(OpenVideoUrl))
                print(OpenVideoUrl)
                self.player.setMedia(QMediaContent(OpenVideoUrl))  # 导入视频
                # self.video_name = OpenFileUrl.fileName()
                # self.video_name = self.video_name[:-4]

                QMessageBox.information(self, "Success!", "视频已导入，请点击“播放”开始播放视频！")

                self.qid.setText(str(self.videoIndex) + "/" + str(len(self.videoList)))
                self.ifImportVideoFirst = 1

                print(self.video_name)

            else:
                QMessageBox.information(self, "Error!", "未找到视频，请将视频放入video文件夹下！")
        else:
            QMessageBox.information(self, "Error!", "您已经导入视频！")

    # 导入question文件
    def playVideo(self):
        if self.ifImportVideoFirst == 1:
            self.player.play()
        else:
            QMessageBox.information(self, "Error!", "请先导入视频！")

    def pauseVideo(self):
        self.player.pause()

    def videoDoubleClicked(self, text):
        if self.player.duration() > 0:  # 开始播放后才允许进行全屏操作
            if self.videoFullScreen:
                self.player.setVideoOutput(self.wgt_video)
                self.videoFullScreenWidget.hide()
                self.videoFullScreen = False
            else:
                self.videoFullScreenWidget.show()
                self.player.setVideoOutput(self.videoFullScreenWidget)
                self.videoFullScreenWidget.setFullScreen(1)
                self.videoFullScreen = True

    def next(self):
        if self.ifImportVideoFirst == 1:
            if self.ifFinished():
                if self.videoIndex < len(self.videoList):
                    self.log = []
                    self.store_log()
                    self.clearAns()
                    self.ans.append(self.log)
                    print(self.ans)

                    self.videoIndex = self.videoIndex + 1
                    self.qid.setText(str(self.videoIndex) + "/" + str(len(self.videoList)))
                    QMessageBox.information(self, "Success!", "答案已保存，请点击”播放“继续观看视频并答题！")
                    self.videoPath = usrConfig.VideoBasePath + '/' + self.videoList[self.videoIndex - 1]
                    OpenVideoUrl = PyQt5.QtCore.QUrl(self.videoPath)
                    self.player.setMedia(QMediaContent(OpenVideoUrl))  # 导入视频
                else:
                    self.log = []
                    self.store_log()
                    if self.videoIndex == len(self.videoList):
                        self.clearAns()
                        self.ans.append(self.log)
                        self.videoIndex = self.videoIndex + 1
                        print(self.ans)
                        print(self.videoIndex)
                    QMessageBox.information(self, "Success!", "答案已保存，视频播放完毕，请点击“导出答案”！")
            else:
                QMessageBox.information(self, "Error!", "题目未全部完成，请先完成所有题目！")

        else:
            QMessageBox.information(self, "Error!", "请先导入视频！")

    def importQue(self):
        # test
        self.load()

    def saveAns(self):
        if self.ifImportVideoFirst == 1:
            if self.videoIndex > len(self.videoList):
                res = store.store_res(self.ans)
                if res[0]:
                    QMessageBox.information(self, "Success!", "答案已导出至csv/results/result.csv！")
                    self.close()
                else:
                    QMessageBox.critical(self, "Error!", "答案导出异常！")
                    self.close()

            else:
                QMessageBox.information(self, "Error!", "请完成所有题目再导出答案！")
        else:
            QMessageBox.information(self, "Error!", "请先导入视频！")


