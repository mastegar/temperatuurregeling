from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from pyqtgraph import PlotWidget, ViewBox

class Ui_MainWindow(object):
	def __init__(self, creator):
		self.main = creator

		# List of strings of the available COM-ports and a list of their UI action elements.
		self.availableCOMs = []
		self.availableCOMActions = []
		self.currentCOM = None
		self.currentBaudrate = 9600

	def setupUi(self, MainWindow):
		self.MainWindow = MainWindow
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1050, 900)
		MainWindow.setMinimumSize(QtCore.QSize(700, 600))
		_translate = QtCore.QCoreApplication.translate

		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.vl_onderkant = QtWidgets.QVBoxLayout()
		self.vl_onderkant.setObjectName("vl_onderkant")
		self.gl_instellingen = QtWidgets.QGridLayout()
		self.gl_instellingen.setObjectName("gl_instellingen")
		self.l_kp = QtWidgets.QLabel(self.centralwidget)
		self.l_kp.setMaximumSize(QtCore.QSize(30, 16777215))
		self.l_kp.setObjectName("l_kp")
		self.gl_instellingen.addWidget(self.l_kp, 1, 2, 1, 1)
		self.line = QtWidgets.QFrame(self.centralwidget)
		self.line.setFrameShape(QtWidgets.QFrame.VLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.gl_instellingen.addWidget(self.line, 1, 1, 3, 1)
		self.pb_start = QtWidgets.QPushButton(self.centralwidget)
		self.pb_start.setObjectName("pb_start")
		self.gl_instellingen.addWidget(self.pb_start, 3, 5, 1, 1)

		self.sp_kp = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.sp_kp.setObjectName("sp_kp")
		self.sp_kp.setMaximum(1000000.00)
		self.gl_instellingen.addWidget(self.sp_kp, 1, 3, 1, 1)
		self.hl_tijdlayout = QtWidgets.QHBoxLayout()
		self.hl_tijdlayout.setObjectName("hl_tijdlayout")
		self.l_tijdlabel = QtWidgets.QLabel(self.centralwidget)
		self.l_tijdlabel.setMinimumSize(QtCore.QSize(50, 16777215))
		self.l_tijdlabel.setMaximumSize(QtCore.QSize(50, 16777215))
		self.l_tijdlabel.setObjectName("l_tijdlabel")
		self.hl_tijdlayout.addWidget(self.l_tijdlabel)
		self.l_tijdwaarde = QtWidgets.QLabel(self.centralwidget)
		self.l_tijdwaarde.setMinimumSize(QtCore.QSize(100, 16777215))
		self.l_tijdwaarde.setObjectName("l_tijdwaarde")
		self.hl_tijdlayout.addWidget(self.l_tijdwaarde)
		self.l_buitenTempLabel = QtWidgets.QLabel(self.centralwidget)
		self.l_buitenTempLabel.setMinimumSize(QtCore.QSize(130, 16777215))
		self.l_buitenTempLabel.setMaximumSize(QtCore.QSize(130, 16777215))
		self.l_buitenTempLabel.setObjectName("l_buitenTempLabel")
		self.hl_tijdlayout.addWidget(self.l_buitenTempLabel)
		self.l_buitenTempWaarde = QtWidgets.QLabel(self.centralwidget)
		self.l_buitenTempWaarde.setMinimumSize(QtCore.QSize(100, 16777215))
		self.l_buitenTempWaarde.setObjectName("l_buitenTempWaarde")
		self.hl_tijdlayout.addWidget(self.l_buitenTempWaarde)


		self.gl_instellingen.addLayout(self.hl_tijdlayout, 1, 5, 1, 1)
		self.l_kd = QtWidgets.QLabel(self.centralwidget)
		self.l_kd.setMaximumSize(QtCore.QSize(30, 16777215))
		self.l_kd.setObjectName("l_kd")
		self.gl_instellingen.addWidget(self.l_kd, 3, 2, 1, 1)
		self.l_ki = QtWidgets.QLabel(self.centralwidget)
		self.l_ki.setMaximumSize(QtCore.QSize(30, 16777215))
		self.l_ki.setObjectName("l_ki")
		self.gl_instellingen.addWidget(self.l_ki, 2, 2, 1, 1)
		self.l_instelwaarde = QtWidgets.QLabel(self.centralwidget)
		self.l_instelwaarde.setObjectName("l_instelwaarde")
		self.gl_instellingen.addWidget(self.l_instelwaarde, 1, 0, 1, 1)

		self.hl_stopclear = QtWidgets.QHBoxLayout()
		self.hl_stopclear.setObjectName("hl_stopclear")
		self.pb_stop = QtWidgets.QPushButton(self.centralwidget)
		self.pb_stop.setObjectName("pb_stop")
		self.pb_new = QtWidgets.QPushButton(self.centralwidget)
		self.pb_new.setObjectName("pb_wissen")
		self.hl_stopclear.addWidget(self.pb_stop)
		self.hl_stopclear.addWidget(self.pb_new)
		self.gl_instellingen.addLayout(self.hl_stopclear, 2, 5, 1, 1)
		self.sp_kd = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.sp_kd.setObjectName("sp_kd")
		self.sp_kd.setMaximum(1000000.00)
		self.gl_instellingen.addWidget(self.sp_kd, 3, 3, 1, 1)
		self.sp_instelwaarde = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.sp_instelwaarde.setObjectName("sp_instelwaarde")
		self.sp_instelwaarde.setKeyboardTracking(False)

		self.gl_instellingen.addWidget(self.sp_instelwaarde, 2, 0, 1, 1)
		self.sp_ki = QtWidgets.QDoubleSpinBox(self.centralwidget)
		self.sp_ki.setObjectName("sp_ki")
		self.sp_ki.setMaximum(1000000.00)
		self.gl_instellingen.addWidget(self.sp_ki, 2, 3, 1, 1)
		self.line_2 = QtWidgets.QFrame(self.centralwidget)
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.gl_instellingen.addWidget(self.line_2, 1, 4, 3, 1)
		self.vl_onderkant.addLayout(self.gl_instellingen)

		# Setting graphing settings.
		pg.setConfigOption('background', 'w')
		pg.setConfigOption('foreground', 'k')
		self.measuredTempPen = pg.mkPen(color=(0, 0, 255), width=2)
		self.setTempPen = pg.mkPen(color=(255,0,0), width=2)
		self.errorPen = pg.mkPen(color=(255,255,0), width=2)
		self.powerPen = pg.mkPen(color=(0,255,0), width=2)

		# Setting up the temperature graph
		self.gv_temperatuur = PlotWidget(self.centralwidget)
		self.gv_temperatuur.setObjectName("gv_temperatuur")
		self.vl_onderkant.addWidget(self.gv_temperatuur)
		self.gv_temperatuur.getPlotItem().setXRange(0, 200)
		self.gv_temperatuur.getPlotItem().setYRange(0, 30)
		self.gv_temperatuur.getPlotItem().getViewBox().setLimits(xMin = 0, yMax = 40, yMin = 15)
		self.gv_temperatuur.getPlotItem().getViewBox().enableAutoRange(ViewBox.XAxis, True)
		self.gv_temperatuur.getPlotItem().setMenuEnabled(False)

		# Setting up the error and power graphs.
		self.hl_ondersteGrafieken = QtWidgets.QHBoxLayout()
		self.hl_ondersteGrafieken.setObjectName("hl_ondersteGrafieken")
		self.gv_vermogen = PlotWidget(self.centralwidget)
		self.gv_vermogen.setObjectName("gv_vermogen")
		self.gv_vermogen.hide()
		self.gv_afwijking = PlotWidget(self.centralwidget)
		self.gv_afwijking.setObjectName("gv_afwijking")
		self.gv_afwijking.hide()
		self.vl_onderkant.addLayout(self.hl_ondersteGrafieken)
		self.verticalLayout_2.addLayout(self.vl_onderkant)

		# Setting up the 'bestand' menu
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
		self.menubar.setObjectName("menubar")
		self.m_bestand = QtWidgets.QMenu(self.menubar)
		self.m_bestand.setObjectName("m_bestand")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.l_status = QtWidgets.QLabel()
		self.statusbar.addPermanentWidget(self.l_status)
		self.update_statusbar_message(False)    # Makes sure a message is shown at the beginning
		self.a_nieuw = QtWidgets.QAction(MainWindow)
		self.a_nieuw.setObjectName("a_nieuw")
		self.a_openen = QtWidgets.QAction(MainWindow)
		self.a_openen.setObjectName("a_openen")
		self.actionOpslaan = QtWidgets.QAction(MainWindow)
		self.actionOpslaan.setObjectName("actionOpslaan")
		self.a_opslaan = QtWidgets.QAction(MainWindow)
		self.a_opslaan.setObjectName("a_opslaan")
		self.a_opslaanAls = QtWidgets.QAction(MainWindow)
		self.a_opslaanAls.setObjectName("a_opslaanAls")
		self.a_exporteren = QtWidgets.QAction(MainWindow)
		self.a_exporteren.setObjectName("a_exporteren")
		self.m_bestand.addAction(self.a_nieuw)
		self.m_bestand.addAction(self.a_openen)
		self.m_bestand.addSeparator()
		self.m_bestand.addAction(self.a_opslaan)
		self.m_bestand.addAction(self.a_opslaanAls)
		self.m_bestand.addSeparator()
		self.m_bestand.addAction(self.a_exporteren)
		self.menubar.addAction(self.m_bestand.menuAction())

		# Setting up the 'instellingen' menu.
		self.m_instelling = QtWidgets.QMenu(self.menubar)
		self.m_instelling.setObjectName("m_instellingen")
		self.a_refreshCOMs = QtWidgets.QAction(MainWindow)
		self.a_refreshCOMs.setObjectName("refreshCOMs")
		self.m_instelling.addAction(self.a_refreshCOMs)
		self.mim_poort = QtWidgets.QMenu(MainWindow)
		self.mim_poort.setObjectName("mim_poort")
		self.m_instelling.addMenu(self.mim_poort)
		self.m_instelling.addSeparator()
		self.mim_baudrate = QtWidgets.QMenu(MainWindow)
		self.mim_baudrate.setObjectName("mim_baudrate")
		baudrates = ["300", "1200", "2400", "4800", "9600", "19200", "38400", "57600", "74880", "115200", "230400", "250000"]
		self.ag_baudrates = QtWidgets.QActionGroup(self.MainWindow)
		self.ag_baudrates.setExclusive(True)
		for br in baudrates:
			a_newBaudrate = QtWidgets.QAction(self.MainWindow)
			a_newBaudrate.setCheckable(True)
			self.ag_baudrates.addAction(a_newBaudrate)
			a_newBaudrate.setText(_translate("MainWindow", br))
			if br == '9600':
				a_newBaudrate.setChecked(True)
				self.currentBaudrate = 9600
			a_newBaudrate.triggered.connect(lambda ignore, brn=br: self.handle_baudrate_selection(int(brn)))  # 'ignore' makes sure the lambda function doesn't use the triggered event's boolean argument.
			self.mim_baudrate.addAction(a_newBaudrate)
		self.m_instelling.addMenu(self.mim_baudrate)
		self.menubar.addAction(self.m_instelling.menuAction())

		# Setting up the 'weergeven' menu.
		self.m_beeld = QtWidgets.QMenu(self.menubar)
		self.m_beeld.setObjectName("m_beeld")
		self.a_toonAfwijking = QtWidgets.QAction(MainWindow)
		self.a_toonAfwijking.setCheckable(True)
		self.a_toonAfwijking.setObjectName("a_toonAfwijking")
		self.a_toonVermogen = QtWidgets.QAction(MainWindow)
		self.a_toonVermogen.setCheckable(True)
		self.a_toonVermogen.setObjectName("a_toonVermogen")
		self.m_beeld.addAction(self.a_toonAfwijking)
		self.m_beeld.addAction(self.a_toonVermogen)
		self.menubar.addAction(self.m_beeld.menuAction())

		# connecting events
		self.sp_instelwaarde.valueChanged.connect(lambda: self.main.change_temperature_goal(self.sp_instelwaarde.value()))
		#self.sp_instelwaarde.editingFinished.connect(self.sp_instelwaarde.clearFocus())
		# lambda: self.main.change_temperature_goal(self.sp_instelwaarde.value())
		self.a_toonAfwijking.toggled.connect(self.afwijking_toggled)
		self.a_toonVermogen.toggled.connect(self.vermogen_toggled)
		self.a_refreshCOMs.triggered.connect(self.on_click_refresh_available_coms)
		self.pb_start.clicked.connect(self.main.start_process)
		self.pb_stop.clicked.connect(self.main.stop_process)
		self.pb_new.clicked.connect(self.main.new)

		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		# Setting the visible name of all components.
		MainWindow.setWindowTitle(_translate("MainWindow", "Temperatuurregeling"))
		self.l_kp.setText(_translate("MainWindow", "Kp"))
		self.pb_start.setText(_translate("MainWindow", "Start"))
		self.l_tijdlabel.setText(_translate("MainWindow", "Tijd:"))
		self.l_buitenTempLabel.setText(_translate("MainWindow", "Temperatuur buiten:"))
		self.l_buitenTempWaarde.setText(_translate("MainWindow", "0"))
		self.l_tijdwaarde.setText(_translate("MainWindow", "0"))
		self.l_kd.setText(_translate("MainWindow", "Kd"))
		self.l_ki.setText(_translate("MainWindow", "Ki"))
		self.l_instelwaarde.setText(_translate("MainWindow", "Instelwaarde:"))
		self.pb_stop.setText(_translate("MainWindow", "Stop"))
		self.pb_new.setText(_translate("MainWindow", "Nieuw"))
		self.m_bestand.setTitle(_translate("MainWindow", "Bestand"))
		self.m_beeld.setTitle(_translate("MainWindow", "Weergeven"))
		self.m_instelling.setTitle(_translate("MainWindow", "Instellingen"))
		self.a_refreshCOMs.setText(_translate("MainWindow", "Poorten vernieuwen"))
		self.mim_poort.setTitle(_translate("MainWindow", "Poort"))
		self.mim_baudrate.setTitle(_translate("MainWindow", "Baudrate"))
		self.a_nieuw.setText(_translate("MainWindow", "Nieuw"))
		self.a_openen.setText(_translate("MainWindow", "Openen"))
		self.actionOpslaan.setText(_translate("MainWindow", "Opslaan"))
		self.a_opslaan.setText(_translate("MainWindow", "Opslaan"))
		self.a_opslaanAls.setText(_translate("MainWindow", "Opslaan Als..."))
		self.a_exporteren.setText(_translate("MainWindow", "Exporteren"))
		self.a_toonVermogen.setText(_translate("MainWindow", "Toon vermogen"))
		self.a_toonAfwijking.setText(_translate("MainWindow", "Toon afwijking"))

		self.post_setup_init()

	def post_setup_init(self):
		self.on_click_refresh_available_coms()

	def vermogen_toggled(self):
		"""Toggles between showing and hiding the power graph"""
		if self.a_toonVermogen.isChecked():
			self.hl_ondersteGrafieken.insertWidget(1, self.gv_vermogen)
			self.gv_vermogen.show()
		else:
			self.hl_ondersteGrafieken.removeWidget(self.gv_vermogen)
			self.gv_vermogen.hide()

	def afwijking_toggled(self):
		"""Toggles between showing and hiding the error graph"""
		if self.a_toonAfwijking.isChecked():
			self.hl_ondersteGrafieken.insertWidget(0,self.gv_afwijking)
			self.gv_afwijking.show()
		else:
			self.hl_ondersteGrafieken.removeWidget(self.gv_afwijking)
			self.gv_afwijking.hide()

	def update_outside_temperature(self, newValue):
		self.l_buitenTempWaarde.setText(newValue)

	def plotNewTemperatureGraph(self, updated_data, setTemp):
		"Plots the current and goal temperature using the newest data"
		self.gv_temperatuur.getPlotItem().clear()
		self.gv_temperatuur.getPlotItem().plot([i for i in range(len(updated_data))], updated_data, pen=self.measuredTempPen)
		self.gv_temperatuur.getPlotItem().addLine(y=setTemp, pen=self.setTempPen)

	def plotNewErrorGraph(self, updated_data):
		"""Plots the error graph using the newest data"""
		self.gv_afwijking.getPlotItem().clear()
		self.gv_afwijking.getPlotItem().plot([i for i in range(len(updated_data))], updated_data, pen=self.errorPen)

	def plotNewPowerGraph(self, updated_data):
		"""Plots the power graph using the newest data"""
		self.gv_vermogen.getPlotItem().clear()
		self.gv_vermogen.getPlotItem().plot([i for i in range(len(updated_data))], updated_data, pen=self.powerPen)

	def clear_all_graphs(self):
		self.gv_temperatuur.getPlotItem().clear()
		self.gv_afwijking.getPlotItem().clear()
		self.gv_vermogen.getPlotItem().clear()

	def lock_settings(self):
		self.sp_instelwaarde.setEnabled(False)
		self.sp_kp.setEnabled(False)
		self.sp_ki.setEnabled(False)
		self.sp_kd.setEnabled(False)

	def unlock_settings(self):
		self.sp_instelwaarde.setEnabled(True)
		self.sp_kp.setEnabled(True)
		self.sp_ki.setEnabled(True)
		self.sp_kd.setEnabled(True)

	def collect_settings(self):
		"""Returns the settings as inputted by the user"""
		return {"setTemp": self.sp_instelwaarde.value(),
		            "Kp": self.sp_kp.value(),
		            "Ki": self.sp_ki.value(),
		            "Kd": self.sp_kd.value()}

	def add_available_coms(self):
		"""Adds the the available COM-ports that were found via on_click_refresh_coms() to the UI-menu"""
		self.availableCOMActions = []
		_translate = QtCore.QCoreApplication.translate
		self.ag_comPorts = QtWidgets.QActionGroup(self.MainWindow)
		self.ag_comPorts.setExclusive(True)
		for i in self.availableCOMs:
			a_newPort = QtWidgets.QAction(self.MainWindow)
			a_newPort.setCheckable(True)
			self.ag_comPorts.addAction(a_newPort)
			self.mim_poort.addAction(a_newPort)
			a_newPort.setText(_translate("MainWindow", i))
			a_newPort.triggered.connect(lambda ignore, use=i: self.handle_com_selection(use))   # 'ignore' makes sure the lambda function doesn't use the triggered event's boolean argument.
			self.availableCOMActions.append(a_newPort)

	def handle_com_selection(self, com):
		"""Updates the current COM and reopens connection"""
		self.currentCOM = com
		opened = self.main.open_com(self.currentCOM, self.currentBaudrate)  # self.main.open_com returns True if connection succeeded.
		if opened:
			validated = self.main.validate_device()
			if not validated: self.main.close_com()
		self.display_new_connection_message(succeeded=validated)
		self.update_statusbar_message(succeeded=validated)

	def on_click_refresh_available_coms(self):
		"""Destroys COM-actions, requests from main the available COMs, initiates the instantiation of new COM-actions"""
		for action in self.availableCOMActions:
			self.mim_poort.removeAction(action)
		self.availableCOMActions = []
		self.availableCOMs = self.main.refresh_available_coms()
		self.add_available_coms()

	def handle_baudrate_selection(self, baudrate):
		"""
		Updates the current baudrate and reopens connection
		baudrate --> int
		"""
		self.currentBaudrate = baudrate
		if not self.currentCOM:
			return
		opened = self.main.open_com(self.currentCOM, self.currentBaudrate)  # self.main.open_com returns True if connection succeeded.
		self.display_new_connection_message(succeeded=opened)
		self.update_statusbar_message(succeeded=opened)

	def display_new_connection_message(self, succeeded):
		self.statusbar.clearMessage()
		if succeeded:
			self.statusbar.showMessage("Een nieuwe verbinding is geopend met " + self.currentCOM + " (" + str(self.currentBaudrate) + ")", 3000)
		else:
			self.statusbar.showMessage("Er kon geen verbinging gemaakt worden met " + self.currentCOM + " (" + str(self.currentBaudrate) + ")", 3000)

	def update_statusbar_message(self, succeeded):
		if succeeded:
			self.l_status.setText("Poort: " + self.currentCOM + "  -  Baudrate: " + str(self.currentBaudrate))
		else:
			self.l_status.setText("Geen verbinding")


