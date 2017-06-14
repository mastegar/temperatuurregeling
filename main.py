import layout, sys, serialManager, time, random
from PyQt5 import QtWidgets, QtCore

class Program(QtCore.QObject):
	def __init__(self):
		super().__init__()
		self.serialPort = serialManager.SerialPort()
		self.availableCOMs = []
		self.refresh_available_coms()
		self.isConnected = False

		self.TiValues = []

		self.data_retrieval_thread = None   # Binnentemperatuur
		self.collecting_data = False
		self.timerClock = None

		self.temperatureData = []
		self.errorData = []
		self.powerData = []
		self.setTemp = 0

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
			self.ui.statusbar.showMessage("Geen COM verbinding...")
			return
		# Send settings to Arduino.
		settings = self.ui.collect_settings()
		self.setTemp = settings['setTemp']
		self.serialPort.send_data('iw', settings['setTemp'])
		self.serialPort.send_data('kp', settings['Kp'])
		self.serialPort.send_data('ki', settings['Ki'])
		self.serialPort.send_data('kd', settings['Kd'])

		self.timerClock = self.TimerClock(self.ui.l_tijdwaarde)
		self.collecting_data = True
		self.data_retrieval_thread = self.DataRetrievalThread(self)
		self.data_retrieval_thread.new_data_signal.connect(self.retrieve_data)
		self.data_retrieval_thread.start()

	def stop_process(self):
		"""Stops the arduino's PID control loop"""
		self.timerClock.zero()

	def clear(self):
		self.timerClock.zero()
		self.temperatureData.clear()
		self.powerData.clear()
		self.errorData.clear()
		self.collecting_data = False

	def change_temperature_goal(self, newGoal):
		self.ui.statusbar.showMessage("Instelwaarde veranderd naar: " + str(newGoal), 3000)
		#print(bytes([int(newGoal)]))
		#self.serialPort.write(bytes([int(newGoal)]))

	def refresh_available_coms(self):
		self.availableCOMs = self.serialPort.get_available_coms()
		return self.availableCOMs

	def validate_partner(self):
		self.serialPort.send_command_await_response('vr.')

	def updateGraphs(self, new_temp_value, new_power_value):
		"""Updates the data for all graphs and redraws the graphs using that data"""
		# Appending the new measurements to the data lists.
		self.temperatureData.append(new_temp_value)
		#self.errorData.append(new_error_value)
		self.powerData.append(new_power_value)

		# Updating the time.
		self.timerClock.increment()

		# Updating the graphs.
		self.ui.plotNewTemperatureGraph(self.temperatureData, self.setTemp)
		#self.ui.plotNewErrorGraph(self.errorData)
		self.ui.plotNewPowerGraph(self.powerData)

	QtCore.pyqtSlot()
	def retrieve_data(self):
		_new_temp_value = int(self.serialPort.send_command_await_response('ti'))/50
		_new_power_value = int(self.serialPort.send_command_await_response('i'))

		self.ui.update_outside_temperature(str(_new_power_value))
		self.updateGraphs(_new_temp_value, _new_power_value)

	class DataRetrievalThread(QtCore.QThread):
		new_data_signal = QtCore.pyqtSignal()

		def __init__(self, creator):
			super().__init__()
			self.creator = creator

		def run(self):
			time1 = time.clock()
			self.new_data_signal.emit()
			total_time = time.clock() - time1
			time.sleep(1 - total_time)
			if self.creator.collecting_data:
				self.run()

	class TimerClock(object):
		def __init__(self, label):
			self.label = label

			self.minutes = 0
			self.seconds = 0

			self.reached_max = False

		def increment(self):
			if self.reached_max:
				return
			self.seconds += 1
			if self.seconds == 60:
				self.seconds = 0
				self.minutes += 1
				if self.minutes == 60: self.reached_max = True
			self.update_label()

		def get_time(self):
			time = ""
			if self.minutes <= 9:
				time += "0"
			time += str(self.minutes)
			time += ":"
			if self.seconds <= 9:
				time += "0"
			time += str(self.seconds)
			return time

		def update_label(self):
			self.label.setText(self.get_time())

		def zero(self):
			self.minutes = 0
			self.seconds = 0
			self.update_label()



if __name__ == "__main__":
	program = Program()
