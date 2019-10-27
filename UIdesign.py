# coding:utf-8

from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import qtawesome as qta

class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # 界面基本结构
        self.setFixedSize(1080,900)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout) # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget,0,0,24,2) # 左侧部件在第0行第0列，占24行3列
        self.main_layout.addWidget(self.right_widget,0,2,24,10) # 右侧部件在第0行第4列，占24行9列
        self.setCentralWidget(self.main_widget) # 设置窗口主部件

        # 左侧菜单栏
        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("简 介")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("队 长")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("队 员")
        self.left_label_3.setObjectName('left_label')
        self.left_label_4 = QtWidgets.QPushButton("经 理")
        self.left_label_4.setObjectName('left_label')
        self.left_label_5 = QtWidgets.QPushButton("教 练")
        self.left_label_5.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qta.icon('fa5s.basketball-ball', color='white'), "计科女篮")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "3  胡梦飞")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "4  周  颖")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "0  姚银银")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "7  孙佳怡")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "10 金海欣")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "11 石  月")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "12 任  玥")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "13 范凌敏")
        self.left_button_9.setObjectName('left_button')
        self.left_button_10 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "16 刘巳祺")
        self.left_button_10.setObjectName('left_button')
        self.left_button_11 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "18 杜彤瑶")
        self.left_button_11.setObjectName('left_button')
        self.left_button_12 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "19 陈梦雪")
        self.left_button_12.setObjectName('left_button')
        self.left_button_13 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "24 汪  悦")
        self.left_button_13.setObjectName('left_button')
        self.left_button_14 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "65 丁思萌")
        self.left_button_14.setObjectName('left_button')
        self.left_button_15 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "85 李雯雯")
        self.left_button_15.setObjectName('left_button')
        self.left_button_16 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "99 王玉美")
        self.left_button_16.setObjectName('left_button')
        self.left_button_17 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "杨云帆")
        self.left_button_17.setObjectName('left_button')
        self.left_button_18 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "王小宇")
        self.left_button_18.setObjectName('left_button')
        self.left_button_19 = QtWidgets.QPushButton(qta.icon('fa5s.caret-right', color='white'), "徐雪健")
        self.left_button_19.setObjectName('left_button')


        # 实现按钮中的Font Awesome字体图标的显示
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)  # 简介
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 3, 0, 1, 3)  # 队长
        self.left_layout.addWidget(self.left_button_2, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 6, 0, 1, 3)  # 队员
        self.left_layout.addWidget(self.left_button_4, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_10, 13, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_11, 14, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_12, 15, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_13, 16, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_14, 17, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_15, 18, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_16, 19, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_4, 20, 0, 1, 3)  # 经理
        self.left_layout.addWidget(self.left_button_17, 21, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_5, 22, 0, 1, 3)  # 教练
        self.left_layout.addWidget(self.left_button_18, 23, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_19, 24, 0, 1, 3)


        # 右侧顶部今日动态模块
        self.right_news_label = QtWidgets.QLabel("今日动态")
        self.right_news_label.setObjectName('right_lable')

        self.right_news_widget = QtWidgets.QWidget()  # 动态部件
        self.right_news_layout = QtWidgets.QGridLayout()  # 今日动态网格布局
        self.right_news_widget.setLayout(self.right_news_layout)

        self.news_button_1 = QtWidgets.QToolButton()
        self.news_button_1.setText("训练通知")  # 设置按钮文本
        self.news_button_1.setIcon(QtGui.QIcon('./img/basketball.png'))  # 设置按钮图标
        self.news_button_1.setIconSize(QtCore.QSize(180, 180))  # 设置图标大小
        self.news_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文

        self.news_button_2 = QtWidgets.QToolButton()
        self.news_button_2.setText("聚众自习")
        self.news_button_2.setIcon(QtGui.QIcon('./img/study.png'))
        self.news_button_2.setIconSize(QtCore.QSize(180, 180))
        self.news_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.news_button_3 = QtWidgets.QToolButton()
        self.news_button_3.setText("视频分析")
        self.news_button_3.setIcon(QtGui.QIcon('./img/conference2.png'))
        self.news_button_3.setIconSize(QtCore.QSize(180, 180))
        self.news_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_news_layout.addWidget(self.news_button_1, 0, 0)
        self.right_news_layout.addWidget(self.news_button_2, 0, 2)
        self.right_news_layout.addWidget(self.news_button_3, 0, 4)

        self.right_layout.addWidget(self.right_news_label, 1, 0, 1, 9)
        self.right_layout.addWidget(self.right_news_widget, 2, 0, 2, 9)

        # 最新战绩和表情包
        self.right_match_lable = QtWidgets.QLabel("最新战绩")
        self.right_match_lable.setObjectName('right_lable')

        self.right_emoji_lable = QtWidgets.QLabel("热门表情包")
        self.right_emoji_lable.setObjectName('right_lable')

        self.right_match_widget = QtWidgets.QWidget()  # 最新战绩部件
        self.right_match_layout = QtWidgets.QGridLayout()  # 最新战绩部件网格布局
        self.right_match_widget.setLayout(self.right_match_layout)

        self.match_button_1 = QtWidgets.QPushButton(qta.icon('fa5s.award', color='grey'),"2019年“三好杯”安徽大学学生篮球联赛 女子组第五名")
        self.match_button_2 = QtWidgets.QPushButton(qta.icon('fa5s.laugh-squint', color='grey'),"2019/10/18    计科vs电子      24:20    计科胜")
        self.match_button_3 = QtWidgets.QPushButton(qta.icon('fa5s.laugh-squint', color='grey'),"2019/10/17    计科vs互联网    24:14    计科胜")
        self.match_button_4 = QtWidgets.QPushButton(qta.icon('fa5s.sad-cry', color='grey'),"2019/10/16    计科vs新传      10:30    计科负")
        self.match_button_5 = QtWidgets.QPushButton(qta.icon('fa5s.laugh-squint', color='grey'),"2019/10/15    计科vs生科      38:11    计科胜")
        self.match_button_6 = QtWidgets.QPushButton(qta.icon('fa5s.laugh-squint', color='grey'),"2019/10/09    计科vs文学      22:18    计科胜")
        self.right_match_layout.addWidget(self.match_button_1, 0, 1, 2, 4)
        self.right_match_layout.addWidget(self.match_button_2, 1, 1, 2, 4)
        self.right_match_layout.addWidget(self.match_button_3, 2, 1, 2, 4)
        self.right_match_layout.addWidget(self.match_button_4, 3, 1, 2, 4)
        self.right_match_layout.addWidget(self.match_button_5, 4, 1, 2, 4)
        self.right_match_layout.addWidget(self.match_button_6, 5, 1, 2, 4)

        # 热门表情包模块
        self.right_emoji_widget = QtWidgets.QWidget()  # 播放歌单部件
        self.right_emoji_layout = QtWidgets.QGridLayout()  # 播放歌单网格布局
        self.right_emoji_widget.setLayout(self.right_emoji_layout)

        self.emoji_button_1 = QtWidgets.QToolButton()
        self.emoji_button_1.setIcon(QtGui.QIcon('./img/1.jpg'))
        self.emoji_button_1.setIconSize(QtCore.QSize(150, 150))
        self.emoji_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.emoji_button_2 = QtWidgets.QToolButton()
        self.emoji_button_2.setIcon(QtGui.QIcon('./img/3.jpg'))
        self.emoji_button_2.setIconSize(QtCore.QSize(150, 150))
        self.emoji_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.emoji_button_3 = QtWidgets.QToolButton()
        self.emoji_button_3.setIcon(QtGui.QIcon('./img/9.jpg'))
        self.emoji_button_3.setIconSize(QtCore.QSize(150, 150))
        self.emoji_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.emoji_button_4 = QtWidgets.QToolButton()
        self.emoji_button_4.setIcon(QtGui.QIcon('./img/10.jpg'))
        self.emoji_button_4.setIconSize(QtCore.QSize(150, 150))
        self.emoji_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_emoji_layout.addWidget(self.emoji_button_1, 0, 0)
        self.right_emoji_layout.addWidget(self.emoji_button_2, 0, 1)
        self.right_emoji_layout.addWidget(self.emoji_button_3, 1, 0)
        self.right_emoji_layout.addWidget(self.emoji_button_4, 1, 1)

        # 开发者
        self.right_develop_lable = QtWidgets.QLabel("开发者信息")
        self.right_develop_lable.setObjectName('right_lable')
        self.right_develop_widget = QtWidgets.QWidget()  # 开发者部件
        self.right_develop_layout = QtWidgets.QGridLayout()  # 开发者部件网格布局
        self.right_develop_widget.setLayout(self.right_develop_layout)
        self.develop_button = QtWidgets.QPushButton(qta.icon('fa5s.code', color='grey'),"  Email: tenmoons@foxmail.com")
        self.right_develop_layout.addWidget(self.develop_button, 5, 4, 2, 4)

        # 添加到右侧功能界面
        self.right_layout.addWidget(self.right_match_lable, 4, 0, 1, 4)
        self.right_layout.addWidget(self.right_emoji_lable, 4, 4, 1, 5)
        self.right_layout.addWidget(self.right_match_widget, 5, 0, 3, 4)
        self.right_layout.addWidget(self.right_emoji_widget, 5, 4, 1, 5)
        self.right_layout.addWidget(self.right_develop_lable, 6, 4, 1, 3)
        self.right_layout.addWidget(self.right_develop_widget, 6, 5, 3, 3)

        # 将窗口控制按钮设置为圆点形式
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        # 设置按钮部件的QSS样式
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:7px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:7px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:7px;}QPushButton:hover{background:green;}''')

        # 将左侧菜单中的按钮和文字颜色设置为白色，并且将按钮的边框去掉
        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')


        # 右侧的部件的进行圆角处理，背景设置为白色。
        # 对各模块标题进行放大处理
        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        # 今日动态、最新战绩、热门表情包模块的美化处理
        self.right_news_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
        self.right_emoji_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')

        #对战绩模块的按钮去除边框，修改字体和颜色
        self.right_match_widget.setStyleSheet('''
            QPushButton{
                border:none;
                color:gray;
                font-size:15px;
                height:40px;
                padding-left:5px;
                padding-right:10px;
                text-align:left;
            }
            QPushButton:hover{
                color:black;
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
            }
        ''')

        # 开发者部件修改模式
        self.right_develop_widget.setStyleSheet('''
            QPushButton{
                border:none;
                color:gray;
                font-size:16px;
                height:40px;
                padding-left:5px;
                padding-right:10px;
                text-align:left;
            }
            QPushButton:hover{
                color:black;
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
            }
        ''')

        # 窗口实现无边框和圆角
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.main_widget.setStyleSheet('''
        QWidget#left_widget{
        background:gray;
        border-top:1px solid white;
        border-bottom:1px solid white;
        border-left:1px solid white;
        border-top-left-radius:10px;
        border-bottom-left-radius:10px;
        }
        ''')

        self.main_layout.setSpacing(0) # 去除间隙


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = UserInterface()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()