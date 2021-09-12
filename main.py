import sys#модуль, который дает информацию о том, как питон взаимодействует с операционкой
from PyQt5 import QtCore, QtGui, QtWidgets#QtCore связи с обектами(размеры, расположение), QtGui для рисования, QtWidgets для создания и работы с виджатами

class MainWindow(QtWidgets.QWidget):#главое окно, в нем прописываеися виджеты, размеры; для того чтобы работало нужен второй класс Mywindow(он внизу)
    def setupUi(self, mainWindow):#в ней все прописвается; mainWindow для прописания главного окна, обработок нажатий
        mainWindow.setWindowTitle("PhisLab")#назавание окна
        mainWindow.resize(1200, 500)#минимальнвй размер (Х, У)
        mainWindow.setFixedHeight(500)#фиксированный размер У
        self.HorizontalLayout = QtWidgets.QHBoxLayout()#горизонтальное расположение
        mainWindow.setLayout(self.HorizontalLayout)#добовляем лаяут в окно
        self.VerticalLayout = QtWidgets.QVBoxLayout()#объявление вертикального лаяута
        self.HorizontalLayout.addLayout(self.VerticalLayout)#добовдение его в горизонтальный лаяут
        self.TheoryBtn = QtWidgets.QPushButton("Теория")#объявление кнопки; здесь будет теория по всем темам
        self.TheoryBtn.setFixedSize(380, 100)#размер кнопки
        self.TheoryBtn.setFont(QtGui.QFont('Arial', 15))#стиль кнопки
        self.VerticalLayout.addWidget(self.TheoryBtn)#добовляем кнопку в вертикальный
        self.TheoryBtn.clicked.connect(mainWindow.openTheory)#обработка нажатия в втором классе прописано что сделать
        self.LabBtn = QtWidgets.QPushButton("Лаборотолки")#сдесь будут анимации, лабораторки
        self.LabBtn.setFixedSize(380, 100)
        self.LabBtn.setFont(QtGui.QFont('Arial', 15))
        self.VerticalLayout.addWidget(self.LabBtn, )
        self.LabBtn.clicked.connect(mainWindow.openLab)
        self.TestBtn = QtWidgets.QPushButton("Тесты")#тетсы по темам
        self.TestBtn.setFixedSize(380, 100)
        self.TestBtn.setFont(QtGui.QFont('Arial', 15))
        self.VerticalLayout.addWidget(self.TestBtn)
        self.TestBtn.clicked.connect(mainWindow.openTest)
        self.GraphBtn = QtWidgets.QPushButton("Построеие графиков")#построение графиков
        self.GraphBtn.setFixedSize(380, 100)
        self.GraphBtn.setFont(QtGui.QFont('Arial', 15))
        self.VerticalLayout.addWidget(self.GraphBtn)
        self.GraphBtn.clicked.connect(mainWindow.openGraph)
        self.SPBtn = QtWidgets.QPushButton("Решение задач")#нейронка по решение задач
        self.SPBtn.setFixedSize(380, 100)
        self.SPBtn.setFont(QtGui.QFont('Arial', 15))
        self.VerticalLayout.addWidget(self.SPBtn)
        self.SPBtn.clicked.connect(mainWindow.openSP)
        self.Label = QtWidgets.QLabel("О Приложении")#метка, я думал там написать о приложении
        self.HorizontalLayout.addWidget(self.Label)




class Theory(QtWidgets.QWidget):#класс в котором список тем, при нажатии на тему открывается ноаое окно; пока что не вся теория
    def setupUi(self, theory):#похожие строчки не буду объяснять =)
        theory.resize(700, 500)
        theory.setWindowTitle("Theory")
        self.gridLayout = QtWidgets.QVBoxLayout()
        theory.setLayout(self.gridLayout)
        self.toolbox = QtWidgets.QToolBox()#откройте теорию и посмотрите, не знаю как объяснить; список закладок
        self.gridLayout.addWidget(self.toolbox)
        self.mex = QtWidgets.QWidget()#подзокладка
        self.mexlayout = QtWidgets.QVBoxLayout()
        self.mex.setLayout(self.mexlayout)
        self.mexbtn = QtWidgets.QPushButton("Механика")
        self.mexlayout.addWidget(self.mexbtn)
        self.mexbtn.clicked.connect(theory.openmex)
        self.mextool = QtWidgets.QToolBox()
        self.mexlayout.addWidget(self.mextool)
        self.kin = QtWidgets.QWidget()
        self.kinlayout = QtWidgets.QVBoxLayout()
        self.kin.setLayout(self.kinlayout)
        self.kinbtn = QtWidgets.QPushButton("Кинематика")
        self.kinlayout.addWidget(self.kinbtn)
        self.kinbtn.clicked.connect(theory.openkin)
        self.basicKin = QtWidgets.QPushButton("Основные понятия кинематики")
        self.kinlayout.addWidget(self.basicKin)
        self.basicKin.clicked.connect(theory.openbck)
        self.rpd = QtWidgets.QPushButton("Равномермерное  прямолинейное движение")
        self.kinlayout.addWidget(self.rpd)
        self.rpd.clicked.connect(theory.openrpd)
        self.rzrpd = QtWidgets.QPushButton("Решение задач на равномерное прямолинейное движение")
        self.kinlayout.addWidget(self.rzrpd)
        self.rzrpd.clicked.connect(theory.openrzrpd)
        self.srs = QtWidgets.QPushButton("Средняя скороть")
        self.kinlayout.addWidget(self.srs)
        self.srs.clicked.connect(theory.opensrs)
        self.rzsrs = QtWidgets.QPushButton("Решение задач на среднюю скорость")
        self.kinlayout.addWidget(self.rzsrs)
        self.rzsrs.clicked.connect(theory.openrzsrs)
        self.ryd = QtWidgets.QPushButton("Равноускоренное движение")
        self.kinlayout.addWidget(self.ryd)
        self.ryd.clicked.connect(theory.openryd)
        self.rzryd = QtWidgets.QPushButton("Решение задач на равноускоренное движение")
        self.kinlayout.addWidget(self.rzryd)
        self.rzryd.clicked.connect(theory.openrzryd)
        self.pod = QtWidgets.QPushButton("Свободное падение. Ускорение свободного падение")
        self.kinlayout.addWidget(self.pod)
        self.pod.clicked.connect(theory.openpod)
        self.rzpod = QtWidgets.QPushButton("Решкние задач на свободное падение")
        self.kinlayout.addWidget(self.rzpod)
        self.rzpod.clicked.connect(theory.openrzpod)
        self.tpg = QtWidgets.QPushButton("Движение тела брошенное горизонтально. Движение тела брошенное под углом к"
                                         " горизонту")
        self.kinlayout.addWidget(self.tpg)
        self.tpg.clicked.connect(theory.opentpg)
        self.rztpg = QtWidgets.QPushButton("Решение задач на движение тела брошенное горизонтально и брошенное под"
                                           " углом к горизонту")
        self.kinlayout.addWidget(self.rztpg)
        self.rztpg.clicked.connect(theory.openrztpg)
        self.okr = QtWidgets.QPushButton("Движение тела по окружности")
        self.kinlayout.addWidget(self.okr)
        self.okr.clicked.connect(theory.openokr)
        self.rzokr = QtWidgets.QPushButton("Решение задач на движение по окружности")
        self.kinlayout.addWidget(self.rzokr)
        self.rzokr.clicked.connect(theory.openrzokr)
        self.mextool.addItem(self.kin, "Кинематика")
        self.din = QtWidgets.QWidget()
        self.dinlayout = QtWidgets.QVBoxLayout()
        self.din.setLayout(self.dinlayout)
        self.mextool.addItem(self.din, "Динамика")
        self.stat = QtWidgets.QWidget()
        self.statlayout = QtWidgets.QVBoxLayout()
        self.stat.setLayout(self.statlayout)
        self.mextool.addItem(self.stat, "Статика")
        self.toolbox.addItem(self.mex, "Механика")
        self.ml = QtWidgets.QWidget()
        self.mllayout = QtWidgets.QVBoxLayout()
        self.ml.setLayout(self.mllayout)
        self.mlbtn = QtWidgets.QPushButton("Молекулярная физика и термодинамика")
        self.mllayout.addWidget(self.mlbtn)
        self.mltool = QtWidgets.QToolBox()
        self.mllayout.addWidget(self.mltool)
        self.mkt = QtWidgets.QWidget()
        self.mktlayout = QtWidgets.QVBoxLayout()
        self.mkt.setLayout(self.mktlayout)
        self.mltool.addItem(self.mkt, "МКТ")
        self.term = QtWidgets.QWidget()
        self.termlayout = QtWidgets.QVBoxLayout()
        self.term.setLayout(self.termlayout)
        self.mltool.addItem(self.term, "Термодинамика")
        self.toolbox.addItem(self.ml, "Молекулярная физика и термодинамика")
        self.ele = QtWidgets.QWidget()
        self.elelayaout = QtWidgets.QVBoxLayout()
        self.ele.setLayout(self.elelayaout)
        self.elebtn = QtWidgets.QPushButton("Электричество и магнитизм")
        self.elelayaout.addWidget(self.elebtn)
        self.eletool = QtWidgets.QToolBox()
        self.elelayaout.addWidget(self.eletool)
        self.elestat = QtWidgets.QWidget()
        self.elestatlayout = QtWidgets.QVBoxLayout()
        self.elestat.setLayout(self.elestatlayout)
        self.eletool.addItem(self.elestat, "Электростатика")
        self.eledin = QtWidgets.QWidget()
        self.eledinlayout = QtWidgets.QVBoxLayout()
        self.eledin.setLayout(self.eledinlayout)
        self.eletool.addItem(self.eledin, "Электродинамика")
        self.elemp = QtWidgets.QWidget()
        self.elemplayout = QtWidgets.QVBoxLayout()
        self.elemp.setLayout(self.elemplayout)
        self.eletool.addItem(self.elemp, "Электромагнитное поле")
        self.pipt = QtWidgets.QWidget()
        self.piptlayout = QtWidgets.QVBoxLayout()
        self.pipt.setLayout(self.piptlayout)
        self.eletool.addItem(self.pipt, "Постоянный и переменный ток")
        self.mgstat = QtWidgets.QWidget()
        self.mgstatlayout = QtWidgets.QVBoxLayout()
        self.mgstat.setLayout(self.mgstatlayout)
        self.eletool.addItem(self.mgstat, "Магнитостатика")
        self.elemi = QtWidgets.QWidget()
        self.elemilayout = QtWidgets.QVBoxLayout()
        self.elemi.setLayout(self.elemilayout)
        self.eletool.addItem(self.elemi, "Электромагнитная индукция")
        self.toolbox.addItem(self.ele, "Электричество и магнитизм")
        self.col = QtWidgets.QWidget()
        self.collayout = QtWidgets.QVBoxLayout()
        self.col.setLayout(self.collayout)
        self.colbtn = QtWidgets.QPushButton("Колебания и волны")
        self.collayout.addWidget(self.colbtn)
        self.coltool = QtWidgets.QToolBox()
        self.collayout.addWidget(self.coltool)
        self.mexcol = QtWidgets.QWidget()
        self.mexcollayout = QtWidgets.QVBoxLayout()
        self.mexcol.setLayout(self.mexcollayout)
        self.coltool.addItem(self.mexcol, "Механические колебания и волны")
        self.elecol = QtWidgets.QWidget()
        self.elecollayout = QtWidgets.QVBoxLayout()
        self.elecol.setLayout(self.elecollayout)
        self.coltool.addItem(self.elecol, "Элекрические колебания и волны")
        self.volopt = QtWidgets.QWidget()
        self.voloptlayout = QtWidgets.QVBoxLayout()
        self.volopt.setLayout(self.voloptlayout)
        self.coltool.addItem(self.volopt, "Волновая оптика")
        self.toolbox.addItem(self.col, "Колебания и волны")
        self.kv = QtWidgets.QWidget()
        self.kvlayout = QtWidgets.QVBoxLayout()
        self.kv.setLayout(self.kvlayout)
        self.kvbtn = QtWidgets.QPushButton("Квантовая физика")
        self.kvlayout.addWidget(self.kvbtn)
        self.kvtool = QtWidgets.QToolBox()
        self.kvlayout.addWidget(self.kvtool)
        self.kvopt = QtWidgets.QWidget()
        self.kvoptlayout = QtWidgets.QVBoxLayout()
        self.kvopt.setLayout(self.kvoptlayout)
        self.kvtool.addItem(self.kvopt, "Квановая оптика")
        self.toolbox.addItem(self.kv, "Квантовая физика")




class Mechanics(QtWidgets.QWidget):#теория по всей механике
    def StrMex(self, start, end):#это я умный =)
        d = ""#из текмт файла берется информация
        with open("Mechanic.txt", encoding="utf-8") as f:
            s = f.readlines()
            for i in range(start):
                s[i] = ""
            for row in range(end+1):
                d+=s[row]
        return d
    def setupUi(self, mechanics):
        mechanics.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        mechanics.setLayout(self.vbox)
        self.mex = self.StrMex(0, 57)
        self.label = QtWidgets.QLabel(self.mex)
        self.vbox.addWidget(self.label)




class Kinematics(Mechanics, QtWidgets.QWidget):#это я еще умней)
    def setupUi(self, kinematics):
        kinematics.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        kinematics.setLayout(self.vbox)
        self.kin = self.StrMex(6, 57)
        self.label = QtWidgets.QLabel(self.kin)
        self.vbox.addWidget(self.label)




class BasikConceptKinematics(Mechanics, QtWidgets.QWidget):
    def setupUi(self, bck):
        bck.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        bck.setLayout(self.vbox)
        self.bck = self.StrMex(8, 23)
        self.label = QtWidgets.QLabel(self.bck)
        self.vbox.addWidget(self.label)




class RPD(Mechanics, QtWidgets.QWidget):
    def setupUi(self, rpd):
        rpd.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        rpd.setLayout(self.vbox)
        self.rpd = self.StrMex(24, 29)
        self.label = QtWidgets.QLabel(self.rpd)
        self.vbox.addWidget(self.label)




class RzRPD(Mechanics, QtWidgets.QWidget):
    def setupUi(self, rzrpd):
        rzrpd.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        rzrpd.setLayout(self.vbox)
        self.rzrpd = self.StrMex(30, 31)
        self.label = QtWidgets.QLabel(self.rzrpd)
        self.vbox.addWidget(self.label)




class Srs(Mechanics, QtWidgets.QWidget):
    def setupUi(self, srs):
        srs.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        srs.setLayout(self.vbox)
        self.srs = self.StrMex(32, 35)
        self.label = QtWidgets.QLabel(self.srs)
        self.vbox.addWidget(self.label)




class RzSrs(Mechanics, QtWidgets.QWidget):
    def setupUi(self, rssrs):
        rssrs.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        rssrs.setLayout(self.vbox)
        self.rzsrs = self.StrMex(36, 37)
        self.label = QtWidgets.QLabel(self.rzsrs)
        self.vbox.addWidget(self.label)




class RYD(Mechanics, QtWidgets.QWidget):
    def setupUi(self, ryd):
        ryd.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        ryd.setLayout(self.vbox)
        self.ryd = self.StrMex(38,43)
        self.label = QtWidgets.QLabel(self.ryd)
        self.vbox.addWidget(self.label)




class RzRYD(Mechanics, QtWidgets.QWidget):
    def setupUi(self, rzryd):
        rzryd.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        rzryd.setLayout(self.vbox)
        self.rzryd = self.StrMex(44, 45)
        self.label = QtWidgets.QLabel(self.rzryd)
        self.vbox.addWidget(self.label)




class Pod(Mechanics, QtWidgets.QWidget):
    def setupUi(self, pod):
        pod.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        pod.setLayout(self.vbox)
        self.pod = self.StrMex(46, 48)
        self.label = QtWidgets.QLabel(self.pod)
        self.vbox.addWidget(self.label)




class RzPod(Mechanics, QtWidgets.QWidget):
    def setupUi(self, rzpod):
        rzpod.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        rzpod.setLayout(self.vbox)
        self.rzpod = self.StrMex(49, 50)
        self.label = QtWidgets.QLabel(self.rzpod)
        self.vbox.addWidget(self.label)




class TPG(Mechanics, QtWidgets.QWidget):
    def setupUi(self, tpg):
        tpg.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        tpg.setLayout(self.vbox)
        self.tpg = self.StrMex(51, 52)
        self.label = QtWidgets.QLabel(self.tpg)
        self.vbox.addWidget(self.label)




class RzTpg(Mechanics, QtWidgets.QWidget):
    def setupUi(self, rztpg):
        rztpg.resize(599, 599)
        self.vbox = QtWidgets.QVBoxLayout()
        rztpg.setLayout(self.vbox)
        self.rztpg = self.StrMex(53, 54)
        self.label = QtWidgets.QLabel(self.rztpg)
        self.vbox.addWidget(self.label)




class Okr(Mechanics, QtWidgets.QWidget):
    def setupUi(self, okr):
        okr.resize(588, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        okr.setLayout(self.vbox)
        self.okr = self.StrMex(55, 56)
        self.label = QtWidgets.QLabel(self.okr)
        self.vbox.addWidget(self.label)




class RzOkr(Mechanics, QtWidgets.QWidget):
    def setupUi(self, rzokr):
        rzokr.resize(599, 599)
        self.vbox = QtWidgets.QVBoxLayout()
        rzokr.setLayout(self.vbox)
        self.rzokr = self.StrMex(57, 57)
        self.label = QtWidgets.QLabel(self.rzokr)
        self.vbox.addWidget(self.label)




class Lab(QtWidgets.QWidget):
    def setupUi(self, lab):
        lab.resize(500, 500)
        lab.setWindowTitle("Laboratory")
        self.gridLayout = QtWidgets.QVBoxLayout()
        lab.setLayout(self.gridLayout)
        self.toolbox = QtWidgets.QToolBox()
        self.gridLayout.addWidget(self.toolbox)
        self.mex = QtWidgets.QWidget()
        self.mexlayout = QtWidgets.QVBoxLayout()
        self.mex.setLayout(self.mexlayout)
        self.mextool = QtWidgets.QToolBox()
        self.mexlayout.addWidget(self.mextool)
        self.kin = QtWidgets.QWidget()
        self.kinlayout = QtWidgets.QVBoxLayout()
        self.kin.setLayout(self.kinlayout)
        self.rpd = QtWidgets.QPushButton("Равноускоренное прямолинейное и равноускоренное движение")
        self.kinlayout.addWidget(self.rpd)
        self.rpd.clicked.connect(lab.openrpdanim)
        self.pod = QtWidgets.QPushButton("Свободное падение")
        self.kinlayout.addWidget(self.pod)
        self.pod.clicked.connect(lab.openpodanim)
        self.gr = QtWidgets.QPushButton("Движение тела брошенного горизонтально")
        self.kinlayout.addWidget(self.gr)
        self.gr.clicked.connect(lab.opengoranim)
        self.ygl = QtWidgets.QPushButton("Движение тела брошенноготпод углом к горизонту")
        self.kinlayout.addWidget(self.ygl)
        self.ygl.clicked.connect(lab.opencoranim)
        self.okr = QtWidgets.QPushButton("Движение по окружности")
        self.kinlayout.addWidget(self.okr)
        self.okr.clicked.connect(lab.openelanim)
        self.mextool.addItem(self.kin, "Кинематика")
        self.din = QtWidgets.QWidget()
        self.dinlayout = QtWidgets.QVBoxLayout()
        self.din.setLayout(self.dinlayout)
        self.mextool.addItem(self.din, "Динамика")
        self.stat = QtWidgets.QWidget()
        self.statlayout = QtWidgets.QVBoxLayout()
        self.stat.setLayout(self.statlayout)
        self.mextool.addItem(self.stat, "Статика")
        self.toolbox.addItem(self.mex, "Механика")
        self.ml = QtWidgets.QWidget()
        self.mllayout = QtWidgets.QVBoxLayout()
        self.ml.setLayout(self.mllayout)
        self.mlbtn = QtWidgets.QPushButton("Молекулярная физика и термодинамика")
        self.mllayout.addWidget(self.mlbtn)
        self.mltool = QtWidgets.QToolBox()
        self.mllayout.addWidget(self.mltool)
        self.mkt = QtWidgets.QWidget()
        self.mktlayout = QtWidgets.QVBoxLayout()
        self.mkt.setLayout(self.mktlayout)
        self.mltool.addItem(self.mkt, "МКТ")
        self.term = QtWidgets.QWidget()
        self.termlayout = QtWidgets.QVBoxLayout()
        self.term.setLayout(self.termlayout)
        self.mltool.addItem(self.term, "Термодинамика")
        self.toolbox.addItem(self.ml, "Молекулярная физика и термодинамика")
        self.ele = QtWidgets.QWidget()
        self.elelayaout = QtWidgets.QVBoxLayout()
        self.ele.setLayout(self.elelayaout)
        self.elebtn = QtWidgets.QPushButton("Электричество и магнитизм")
        self.elelayaout.addWidget(self.elebtn)
        self.eletool = QtWidgets.QToolBox()
        self.elelayaout.addWidget(self.eletool)
        self.elestat = QtWidgets.QWidget()
        self.elestatlayout = QtWidgets.QVBoxLayout()
        self.elestat.setLayout(self.elestatlayout)
        self.eletool.addItem(self.elestat, "Электростатика")
        self.eledin = QtWidgets.QWidget()
        self.eledinlayout = QtWidgets.QVBoxLayout()
        self.eledin.setLayout(self.eledinlayout)
        self.eletool.addItem(self.eledin, "Электродинамика")
        self.elemp = QtWidgets.QWidget()
        self.elemplayout = QtWidgets.QVBoxLayout()
        self.elemp.setLayout(self.elemplayout)
        self.eletool.addItem(self.elemp, "Электромагнитное поле")
        self.pipt = QtWidgets.QWidget()
        self.piptlayout = QtWidgets.QVBoxLayout()
        self.pipt.setLayout(self.piptlayout)
        self.eletool.addItem(self.pipt, "Постоянный и переменный ток")
        self.mgstat = QtWidgets.QWidget()
        self.mgstatlayout = QtWidgets.QVBoxLayout()
        self.mgstat.setLayout(self.mgstatlayout)
        self.eletool.addItem(self.mgstat, "Магнитостатика")
        self.elemi = QtWidgets.QWidget()
        self.elemilayout = QtWidgets.QVBoxLayout()
        self.elemi.setLayout(self.elemilayout)
        self.eletool.addItem(self.elemi, "Электромагнитная индукция")
        self.toolbox.addItem(self.ele, "Электричество и магнитизм")
        self.col = QtWidgets.QWidget()
        self.collayout = QtWidgets.QVBoxLayout()
        self.col.setLayout(self.collayout)
        self.colbtn = QtWidgets.QPushButton("Колебания и волны")
        self.collayout.addWidget(self.colbtn)
        self.coltool = QtWidgets.QToolBox()
        self.collayout.addWidget(self.coltool)
        self.mexcol = QtWidgets.QWidget()
        self.mexcollayout = QtWidgets.QVBoxLayout()
        self.mexcol.setLayout(self.mexcollayout)
        self.coltool.addItem(self.mexcol, "Механические колебания и волны")
        self.elecol = QtWidgets.QWidget()
        self.elecollayout = QtWidgets.QVBoxLayout()
        self.elecol.setLayout(self.elecollayout)
        self.coltool.addItem(self.elecol, "Элекрические колебания и волны")
        self.volopt = QtWidgets.QWidget()
        self.voloptlayout = QtWidgets.QVBoxLayout()
        self.volopt.setLayout(self.voloptlayout)
        self.coltool.addItem(self.volopt, "Волновая оптика")
        self.toolbox.addItem(self.col, "Колебания и волны")
        self.kv = QtWidgets.QWidget()
        self.kvlayout = QtWidgets.QVBoxLayout()
        self.kv.setLayout(self.kvlayout)
        self.kvbtn = QtWidgets.QPushButton("Квантовая физика")
        self.kvlayout.addWidget(self.kvbtn)
        self.kvtool = QtWidgets.QToolBox()
        self.kvlayout.addWidget(self.kvtool)
        self.kvopt = QtWidgets.QWidget()
        self.kvoptlayout = QtWidgets.QVBoxLayout()
        self.kvopt.setLayout(self.kvoptlayout)
        self.kvtool.addItem(self.kvopt, "Квановая оптика")
        self.toolbox.addItem(self.kv, "Квантовая физика")




class RPDAnimation(QtWidgets.QWidget):#главное окно по первой анимации, которой пока нет
    def setupUI(self, rpd):
        rpd.setFixedSize(1500, 800)
        self.vbox = QtWidgets.QGridLayout()
        rpd.setLayout(self.vbox)
        self.view = RPDAnimationView()
        self.vbox.addWidget(self.view, 0,0, 0,-1)
        self.startspeededit = QtWidgets.QLineEdit("Началььная скорость")
        self.startspeed = self.startspeededit.text()
        self.vbox.addWidget(self.startspeededit, 1,0)
        self.speededit = QtWidgets.QLineEdit("0")
        self.speed = self.speededit.text()
        self.vbox.addWidget(self.speededit, 2,0)
        self.accedit = QtWidgets.QLineEdit("Ускорение")
        self.acc = self.startspeededit.inputMask()
        self.vbox.addWidget(self.accedit, 3,0)
        self.distedit = QtWidgets.QLineEdit("0")
        self.dist = self.distedit.inputMask()
        self.vbox.addWidget(self.distedit, 1,1, 1,-1)
        self.timeedit = QtWidgets.QLineEdit("Время")
        self.time = self.startspeededit.inputMask()
        self.vbox.addWidget(self.timeedit, 2,1, 2,-1)
        self.startbtn = QtWidgets.QPushButton("Start")
        self.vbox.addWidget(self.startbtn, 3,1)
        self.stopbtn = QtWidgets.QPushButton("Stop")
        self.vbox.addWidget(self.stopbtn, 3,2)





class RPDAnimationView(QtWidgets.QGraphicsView):#общая картина
    def __init__(self):
        super(RPDAnimationView, self).__init__()
        self.sc = RPDAnimationScene()#чать картины
        self.setScene(self.sc)#добовление части




class RPDAnimationScene(QtWidgets.QGraphicsScene):#часть картины
    def __init__(self):
        super(RPDAnimationScene, self).__init__()
        self.dist = 1500#хз зачем
        self.setSceneRect(0, 0, 1500,600)#размеры картины
        self.fillscene()
    def fillscene(self):#для обрабоки айтема
        self.item=RPDAnimationItem()#вызов айтома
        self.addItem(self.item)#добовление
    def drawBackground(self, painter, rec):#задний фон, здесь я тоже умный =)
        painter.setPen(QtGui.QPen(QtCore.Qt.black, 2))#задаем параметры кисти
        painter.drawLine(0,self.height()-20, self.width(), self.height()-20 )#рисует горизонтальную линию
        x = 0
        painter.setPen(QtGui.QPen(QtCore.Qt.black, 1))#задаем другие параметры кистс
        while x <= self.dist:#циул дл ячерточек и цифорок
            painter.drawLine(x+30,self.height()-15, x+30,self.height()-25)
            painter.drawText(x+30, self.height()-20, 30,30, 1, str(x))
            x+=30




class RPDAnimationItem(QtWidgets.QGraphicsItem, RPDAnimation):#айтем
    def __init__(self):
        super().__init__()
    def boundingRect(self):#обязательная функция
        return QtCore.QRectF(30, 488, 290, 91)#размер обекта
    def paint(self, painter, options, widget):#обязательная фнкция
        painter.setPen(QtGui.QPen(QtCore.Qt.gray, 3))
        painter.drawRect(30,480, 210,70)#рисует прямокгольник
        painter.drawEllipse(30,550,30,30)#круг
        painter.drawEllipse(210, 550, 30, 30)
    def calc(self):#долго думал как заставить двигаться, не получилось
        return 1

        #elif not(self.startspeed.isalpha()) and not(self.dist.isalpha()):



#кроме первого окна с анимацией нисего не седлано

class PodAnimation(QtWidgets.QGraphicsView):
    def setupUi(self, pod):
        self.sc = QtWidgets.QGraphicsScene()
        pod.setScene(self.sc)




class GorizontalAnimation(QtWidgets.QGraphicsView):
    def setepUi(self, gor):
        self.sc = QtWidgets.QGraphicsScene()
        gor.setScene(self.sc)




class CornerAnimation(QtWidgets.QGraphicsView):
    def setupUi(self, cor):
        self.sc = QtWidgets.QGraphicsScene()
        cor.setScene(self.sc)




class ElipsAnimation(QtWidgets.QGraphicsView):
    def setupUi(self, el):
        self.sc = QtWidgets.QGraphicsScene()
        el.setScene(self.sc)




class Test(QtWidgets.QWidget):
    def setupUi(self, test):
        test.resize(234, 234)





class Graph(QtWidgets.QWidget):
    def setupUi(self, graph):
        test.resize(234, 433)




class SolvProblem(QtWidgets.QWidget):
    def setupUi(self, solvProblem):
        solvProblem.resize(242,543)




class MyTheory(QtWidgets.QWidget):#класс в котором обрабатывается открытие теории; сначала открывается этот класс
    def __init__(self):
        super().__init__()
        self.ui = Theory()#потом открывается этот с виджатами
        self.ui.setupUi(self)
    def openmex(self):
        self.exMechanics = MyMechanics()
        self.exMechanics.show()
    def openkin(self):
        self.exKinematics = MyKinematics()
        self.exKinematics.show()
    def openbck(self):
        self.exbck = MyBasicConceptKinematics()
        self.exbck.show()
    def openrpd(self):
        self.exrpd = MyRPD()
        self.exrpd.show()
    def openrzrpd(self):
        self.exrzrpd = MyRzRPD()
        self.exrzrpd.show()
    def opensrs(self):
        self.exsrs = MySrs()
        self.exsrs.show()
    def openrzsrs(self):
        self.exrzsrs = MyRzsrs()
        self.exrzsrs.show()
    def openryd(self):
        self.exryd = Myryd()
        self.exryd.show()
    def openrzryd(self):
        self.exrzryd = Myrzryd()
        self.exrzryd.show()
    def openpod(self):
        self.expod = Mypod()
        self.expod.show()
    def openrzpod(self):
        self.exrzpod = MyRzPod()
        self.exrzpod.show()
    def opentpg(self):
        self.extpg = MyTPG()
        self.extpg.show()
    def openrztpg(self):
        self.exrztpg = MyRzTpg()
        self.exrztpg.show()
    def openokr(self):
        self.exokr = MyOkr()
        self.exokr.show()
    def openrzokr(self):
        self.exrzokr = MyRzOkr()
        self.exrzokr.show()




class MyMechanics(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Mechanics()
        self.ui.setupUi(self)





class MyKinematics(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Kinematics()
        self.ui.setupUi(self)




class MyBasicConceptKinematics(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = BasikConceptKinematics()
        self.ui.setupUi(self)




class MyRPD(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = RPD()
        self.ui.setupUi(self)




class MyRzRPD(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = RzRPD()
        self.ui.setupUi(self)




class MySrs(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Srs()
        self.ui.setupUi(self)




class MyRzsrs(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = RzSrs()
        self.ui.setupUi(self)




class Myryd(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = RYD()
        self.ui.setupUi(self)




class Myrzryd(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = RzRYD()
        self.ui.setupUi(self)




class Mypod(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Pod()
        self.ui.setupUi(self)




class MyRzPod(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = RzPod()
        self.ui.setupUi(self)




class MyTPG(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = TPG()
        self.ui.setupUi(self)




class MyRzTpg(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = RzTpg()
        self.ui.setupUi(self)




class MyOkr(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Okr()
        self.ui.setupUi(self)




class MyRzOkr(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = RzOkr()
        self.ui.setupUi(self)




class MyLab(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Lab()
        self.ui.setupUi(self)
    def openrpdanim(self):
        self.exrpdanim = MyRPDAnimation()
        self.exrpdanim.show()
    def openpodanim(self):
        self.expodanim = MyPodAnimation()
        self.expodanim.show()
    def opengoranim(self):
        self.exroranim = MyGorAnimation()
        self.exroranim.show()
    def opencoranim(self):
        self.excoranim = MyCornAnimtion()
        self.excoranim.show()
    def openelanim(self):
        self.exelanim = MyElAnimation()
        self.exelanim.show()




class MyRPDAnimation(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = RPDAnimation()
        self.ui.setupUI(self)




class MyPodAnimation(QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        self.ui = PodAnimation()
        self.ui.setupUi(self)




class MyGorAnimation(QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        self.ui = GorizontalAnimation()
        self.ui.setepUi(self)




class MyCornAnimtion(QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        self.ui = CornerAnimation()
        self.ui.setupUi(self)




class MyElAnimation(QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        self.ui = ElipsAnimation()
        self.ui.setupUi(self)
#sifisfi



class MyWindow(QtWidgets.QWidget):#самое преое окно, которое отерывается при запуске программы
    def __init__(self):
        super().__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)
    def openTheory(self):
        self.exTheory = MyTheory()
        self.exTheory.show()
    def openLab(self):
        self.exLab = MyLab()
        self.exLab.show()
    def openTest(self):
        self.exTest = Test()
        self.exTest.show()
    def openGraph(self):
        self.exGraph = Graph()
        self.exGraph.show()
    def openSP(self):
        self.exSP = SolvProblem()
        self.exSP.show()
#



if __name__ == '__main__':#это для запуска окон
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
