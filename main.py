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
        self.rzrpd = QtWidgets.QPushButton("Решение задач на равномерное прямолинейное движение")
        self.kinlayout.addWidget(self.rzrpd)
        self.srs = QtWidgets.QPushButton("Средняя скороть")
        self.kinlayout.addWidget(self.srs)
        self.rzsrs = QtWidgets.QPushButton("Решение задач на среднюю скорость")
        self.kinlayout.addWidget(self.rzsrs)
        self.ryd = QtWidgets.QPushButton("Равноускоренное движение")
        self.kinlayout.addWidget(self.ryd)
        self.rzryd = QtWidgets.QPushButton("Решение задач на равноускоренное движение")
        self.kinlayout.addWidget(self.rzryd)
        self.pod = QtWidgets.QPushButton("Свободное падение. Ускорение свободного падение")
        self.kinlayout.addWidget(self.pod)
        self.rzpod = QtWidgets.QPushButton("Решкние задач на свободное падение")
        self.kinlayout.addWidget(self.rzpod)
        self.tpg = QtWidgets.QPushButton("Движение тела брошенное горизонтально. Движение тела брошенное под углом к"
                                         " горизонту")
        self.kinlayout.addWidget(self.tpg)
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
        self.label =QtWidgets.QLabel(f.read())
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
