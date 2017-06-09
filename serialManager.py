import serial, sys, glob

class SerialPort(serial.Serial):
	def __init__(self):
		super().__init__()
		#self.timeout = 2

	def get_available_coms(self):
		""" Lists serial port names

			:raises EnvironmentError:
				On unsupported or unknown platforms
			:returns:
				A list of the serial ports available on the system
		"""
		if sys.platform.startswith('win'):
			ports = ['COM%s' % (i + 1) for i in range(256)]
		elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
			# this excludes your current terminal "/dev/tty"
			ports = glob.glob('/dev/tty[A-Za-z]*')
		elif sys.platform.startswith('darwin'):
			ports = glob.glob('/dev/tty.*')
		else:
			raise EnvironmentError('Unsupported platform')

		result = []
		for port in ports:
			try:
				s = serial.Serial(port)
				s.close()
				result.append(port)
			except (OSError, serial.SerialException):
				pass
		return result

	def send_command_await_response(self, command):
		command = command + '.'
		self.write(command.encode())
		response = self.read_until(b'.').decode()
		response = response[:-1]    # Remove the point.
		return response

	def send_data(self, identifier, value):
		self.write((str(identifier)+'.').encode())
		self.write((str(value)+'.').encode())





