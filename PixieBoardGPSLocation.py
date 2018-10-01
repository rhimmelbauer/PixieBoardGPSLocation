import subprocess


class PixieBoardGPSLocation():
	PIXIE_BOARDS_PASSWORD = "pixiepro"

	COMMAND_OK_CALLBACK = "OK"

	ENABLE_AT_COMMAND = "echo 'ATE1' | socat - /dev/ttyUSB2,cr | grep 'OK'"

	CONFIGURE_GPS_TRACKING = "echo 'AT+QGPS=1,30,50,0,1' | socat - /dev/ttyUSB2,cr | grep 'OK'"

	GET_GPS_LOCATION = "echo 'AT+QGPSLOC?' | socat - /dev/ttyUSB2,cr"

	GET_GPS_LOCATION_PRETTY = "echo 'AT+QGPSLOC=2' | socat - /dev/ttyUSB2,cr"

	def __init__(self):
		self.ModemStatus = ""

		self.UTCTime = ""
		self.Latitude = ""
		self.Longitude = ""
		self.HorizontalPrecision = ""
		self.Altitude = ""
		self.Fix = ""
		self.Cog = ""
		self.SpeedOverGroundKmH = ""
		self.SpeedOverGroundKnots = ""
		self.Date = ""
		self.NumberOfSatellites = ""

	def EnableATCommands():
		command = subprocess.Popen([ENABLE_AT_COMMAND], stdout=subprocess.PIPE, shell=True)
		(command_output, error) = command.communicate(PIXIE_BOARDS_PASSWORD)
		if command_output == COMMAND_OK_CALLBACK:
			return True, command_output, error
		else:
			return False, command_output, error

	def ConfigureGPSTracking():
		command = subprocess.Popen([CONFIGURE_GPS_TRACKING], stdout=subprocess.PIPE, shell=True)
		(command_output, error) = command.communicate(PIXIE_BOARDS_PASSWORD)
		if command_output == COMMAND_OK_CALLBACK:
			return True
		else:
			return False

	def GetGPSLocation():
		command = subprocess.Popen([GET_GPS_LOCATION], stdout=subprocess.PIPE, shell=True)
		(command_output, error) = command.communicate(PIXIE_BOARDS_PASSWORD)

	def GetGPSLocationPretty():
		command = subprocess.Popen([GET_GPS_LOCATION_PRETTY], stdout=subprocess.PIPE, shell=True)
		(command_output, error) = command.communicate(PIXIE_BOARDS_PASSWORD)

	def ParseGPSLocation(command_output):
		locationData = command_output.split(",")
		self.UTCTime = locationData[0][9:]
		self.Latitude = locationData[1]
		self.Longitude = locationData[2]
		self.HorizontalPrecision = locationData[3]
		self.Altitude = locationData[4]
		self.Fix = locationData[5]
		self.Cog = locationData[6]
		self.SpeedOverGroundKmH = locationData[7]
		self.SpeedOverGroundKnots = locationData[8]
		self.Date = locationData[9]
		self.NumberOfSatellites = locationData[10]


