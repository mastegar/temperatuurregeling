import layout, sys, serialManager
from PyQt5 import QtWidgets

class Program(object):
	def __init__(self):
		self.serialPort = serialManager.SerialPort()
		self.availableCOMs = []
		self.refresh_available_coms()

		self.start_ui()

	def start_ui(self):
		"""Initializes and then shows the UI"""
		app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QMainWindow()
		self.ui = layout.Ui_MainWindow(self)
		self.ui.setupUi(MainWindow)
		MainWindow.show()
		sys.exit(app.exec_())

	def start_process(self):
		settings = self.ui.collect_settings()
		print (settings)

	def open_com(self, com, baudrate):
		try:
			self.serialPort.close()
			self.serialPort.port = com
			self.serialPort.baudrate = baudrate
			self.serialPort.open()
			return True
		except:
			return False

	def change_temperature_goal(self, newGoal):
		self.ui.statusbar.showMessage("Instelwaarde veranderd naar: " + str(newGoal), 3000)
		#print(bytes([int(newGoal)]))
		#self.serialPort.write(bytes([int(newGoal)]))

	def refresh_available_coms(self):
		self.availableCOMs = self.serialPort.get_available_coms()
		return self.availableCOMs



if __name__ == "__main__":
	program = Program()
