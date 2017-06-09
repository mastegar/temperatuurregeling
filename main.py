import layout, sys, serialManager, time, threading
from PyQt5 import QtWidgets, QtCore

class Program(object):
	def __init__(self):
		self.serialPort = serialManager.SerialPort()
		self.availableCOMs = []
		self.refresh_available_coms()
		self.isConnected = False

		self.TiValues = []

		self.start_ui()

	def start_ui(self):
		"""Initializes and then shows the UI"""
		self.app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QMainWindow()
		self.ui = layout.Ui_MainWindow(self)
		self.ui.setupUi(MainWindow)
		MainWindow.show()
		sys.exit(self.app.exec_())

	def open_com(self, com, baudrate):
		try:
			self.serialPort.close()
			self.serialPort.port = com
			self.serialPort.baudrate = baudrate
			self.serialPort.open()
		except:
			self.isConnected = False
			return False
		else:
			time.sleep(3)               # Wait for COM to fully open.
			self.isConnected = True
			return True

	def validate_device(self):
		"""
		Checks if the temperatuurregelingspracticum is connected and nothing else.
		:return: True if the correct device is connected
		"""
		return self.serialPort.send_command_await_response('validate') == 'valid'

	def close_com(self):
		self.serialPort.close()
		self.isConnected = False

	def start_process(self):
		if not self.isConnected:
			return
		# Send settings to Arduino.
		settings = self.ui.collect_settings()
		self.serialPort.send_data('iw', settings['setTemp'])
		self.serialPort.send_data('kp', settings['Kp'])
		self.serialPort.send_data('ki', settings['Ki'])
		self.serialPort.send_data('kd', settings['Kd'])
		t = threading.Thread(target=self.start_temperature_retrieval())
		t.start()

	def start_temperature_retrieval(self):
		thread = TemperatureRetrieval()
		thread.finished.connect(self.app.exit)
		thread.start()


	def change_temperature_goal(self, newGoal):
		self.ui.statusbar.showMessage("Instelwaarde veranderd naar: " + str(newGoal), 3000)
		#print(bytes([int(newGoal)]))
		#self.serialPort.write(bytes([int(newGoal)]))

	def refresh_available_coms(self):
		self.availableCOMs = self.serialPort.get_available_coms()
		return self.availableCOMs

	def validate_partner(self):
		self.serialPort.send_command_await_response('vr.')

class TemperatureRetrieval(QtCore.QThread):
	def run(self):
		time1 = time.clock()
		print(self.serialPort.send_command_await_response('ti'))
		totaltime = time.clock() - time1
		time.sleep(1 - totaltime)
		self.run()



if __name__ == "__main__":
	program = Program()
