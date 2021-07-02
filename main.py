import sys
import codecs
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QWidget):
    def setupUi(self, mainWindow):
        mainWindow.setWindowTitle("PhisLab")
        mainWindow.resize(1200, 500)
        mainWindow.setFixedHeight(500)
        self.HorizontalLayout = QtWidgets.QHBoxLayout()
        mainWindow.setLayout(self.HorizontalLayout)
        self.VerticalLayout = QtWidgets.QVBoxLayout()
        self.HorizontalLayout.addLayout(self.VerticalLayout)
        self.TheoryBtn = QtWidgets.QPushButton("Теория")
        self.TheoryBtn.setFixedSize(380, 100)
        self.TheoryBtn.setFont(QtGui.QFont('Arial', 15))
        self.VerticalLayout.addWidget(self.TheoryBtn)
        self.TheoryBtn.clicked.connect(mainWindow.openTheory)
        self.LabBtn = QtWidgets.QPushButton("Лаборотолки")
        self.LabBtn.setFixedSize(380, 100)
        self.LabBtn.setFont(QtGui.QFont('Arial', 15))
        self.VerticalLayout.addWidget(self.LabBtn, )
        self.LabBtn.clicked.connect(mainWindow.openLab)
        self.TestBtn = QtWidgets.QPushButton("Тесты")
        self.TestBtn.setFixedSize(380, 100)
        self.TestBtn.setFont(QtGui.QFont('Arial', 15))
        self.VerticalLayout.addWidget(self.TestBtn)
        self.TestBtn.clicked.connect(mainWindow.openTest)
        self.GraphBtn = QtWidgets.QPushButton("Построеие графиков")
        self.GraphBtn.setFixedSize(380, 100)
        self.GraphBtn.setFont(QtGui.QFont('Arial', 15))
        self.VerticalLayout.addWidget(self.GraphBtn)
        self.GraphBtn.clicked.connect(mainWindow.openGraph)
        self.SPBtn = QtWidgets.QPushButton("Решение задач")
        self.SPBtn.setFixedSize(380, 100)
        self.SPBtn.setFont(QtGui.QFont('Arial', 15))
        self.VerticalLayout.addWidget(self.SPBtn)
        self.SPBtn.clicked.connect(mainWindow.openSP)
        self.Label = QtWidgets.QLabel("О Приложении")
        self.HorizontalLayout.addWidget(self.Label)




class Theory(QtWidgets.QWidget):
    def setupUi(self, theory):
        theory.resize(700, 500)
        theory.setWindowTitle("Theory")
        self.gridLayout = QtWidgets.QVBoxLayout()
        theory.setLayout(self.gridLayout)
        self.toolbox = QtWidgets.QToolBox()
        self.gridLayout.addWidget(self.toolbox)
        self.mex = QtWidgets.QWidget()
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
        self.okr = QtWidgets.QPushButton("Движение тела по окружности")
        self.kinlayout.addWidget(self.okr)
        self.rzokr = QtWidgets.QPushButton("Решение задач на движение по окружности")
        self.kinlayout.addWidget(self.rzokr)
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




class Mechanics(QtWidgets.QWidget):
    def setupUi(self, mechanics):
        mechanics.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        mechanics.setLayout(self.vbox)
        f = codecs.open("Mechanic.txt", encoding="utf-8")
        self.label = QtWidgets.QLabel(f.read())
        self.vbox.addWidget(self.label)
        f.close()




class Kinematics(QtWidgets.QWidget):
    def setupUi(self, kinematics):
        kinematics.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        kinematics.setLayout(self.vbox)
        f = codecs.open("Kinematics.txt", encoding="utf-8")
        self.label = QtWidgets.QLabel(f.read())
        self.vbox.addWidget(self.label)
        f.close()




class BasikConceptKinematics(QtWidgets.QWidget):
    def setupUi(self, bck):
        bck.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        bck.setLayout(self.vbox)
        f = codecs.open("BasicConceptKinematics.txt", encoding="utf-8")
        self.label = QtWidgets.QLabel(f.read())
        self.vbox.addWidget(self.label)
        f.close()




class RPD(QtWidgets.QWidget):
    def setupUi(self, rpd):
        rpd.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        rpd.setLayout(self.vbox)
        f = codecs.open("RPD.txt", encoding="utf-8")
        self.label = QtWidgets.QLabel(f.read())
        self.vbox.addWidget(self.label)
        f.close()




class RzRPD(QtWidgets.QWidget):
    def setupUi(self, rzrpd):
        rzrpd.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        rzrpd.setLayout(self.vbox)
        f = codecs.open("RzRPD.txt", encoding="utf-8")
        self.label = QtWidgets.QLabel(f.read())
        self.vbox.addWidget(self.label)
        f.close()




class Srs(QtWidgets.QWidget):
    def setupUi(self, srs):
        srs.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        srs.setLayout(self.vbox)
        f = codecs.open("srs.txt", encoding="utf-8")
        self.label = QtWidgets.QLabel(f.read())
        self.vbox.addWidget(self.label)
        f.close()




class RzSrs(QtWidgets.QWidget):
    def setupUi(self, rssrs):
        rssrs.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        rssrs.setLayout(self.vbox)
        f = codecs.open("Rzsrs.txt", encoding="utf-8")
        self.label = QtWidgets.QLabel(f.read())
        self.vbox.addWidget(self.label)
        f.close()




class RYD(QtWidgets.QWidget):
    def setupUi(self, ryd):
        ryd.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        ryd.setLayout(self.vbox)
        f = codecs.open("RYD.txt", encoding="utf-8")
        self.label = QtWidgets.QLabel(f.read())
        self.vbox.addWidget(self.label)
        f.close()




class RzRYD(QtWidgets.QWidget):
    def setupUi(self, rzryd):
        rzryd.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        rzryd.setLayout(self.vbox)
        f = codecs.open("RzRYD.txt", encoding="utf-8")
        self.label = QtWidgets.QLabel(f.read())
        self.vbox.addWidget(self.label)
        f.close()




class Pod(QtWidgets.QWidget):
    def setupUi(self, pod):
        pod.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        pod.setLayout(self.vbox)
        f = codecs.open("pod,.txt", encoding="utf-8")
        self.label = QtWidgets.QLabel(f.read())
        self.vbox.addWidget(self.label)
        f.close()




class RzPod(QtWidgets.QWidget):
    def setupUi(self, rzpod):
        rzpod.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        rzpod.setLayout(self.vbox)
        f = codecs.open("RzPod.txt", encoding="utf-8")
        self.label = QtWidgets.QLabel(f.read())
        self.vbox.addWidget(self.label)
        f.close()




class TPG(QtWidgets.QWidget):
    def setupUi(self, tpg):
        tpg.resize(500, 500)
        self.vbox = QtWidgets.QVBoxLayout()
        tpg.setLayout(self.vbox)
        f = codecs.open("TPG.txt", encoding="utf-8")
        self.label = QtWidgets.QLabel(f.read())
        self.vbox.addWidget(self.label)
        f.close()




class Lab(QtWidgets.QWidget):
    def setupUi(self, lab):
        lab.resize(345, 345)




class Test(QtWidgets.QWidget):
    def setupUi(self, test):
        test.resize(234, 234)





class Graph(QtWidgets.QWidget):
    def setupUi(self, graph):
        test.resize(234, 433)




class SolvProblem(QtWidgets.QWidget):
    def setupUi(self, solvProblem):
        solvProblem.resize(242,543)




class MyTheory(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Theory()
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




class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = MainWindow()
        self.ui.setupUi(self)
    def openTheory(self):
        self.exTheory = MyTheory()
        self.exTheory.show()
    def openLab(self):
        self.exLab = Lab()
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




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
