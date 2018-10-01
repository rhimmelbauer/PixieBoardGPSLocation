from PixieBoardGPSLocation import PixieBoardGPSLocation

def TestEnableATCommands():
	pxbdGPSLocation = PixieBoardGPSLocation()
	isEnabled, raw, error = pxbdGPSLocation.EnableATCommands()
	testResult = ""
	print("Enabled: {}\n Output: {}\n Error: {}".format(isEnabled, raw, error))
	

def TestConfigureGPSLocation():
	testResult = ""
	print(testResult)

def TestGetGPSLocation():
	testResult = ""
	print(testResult)

def TestGetGPSLocationPretty():
	testResult = ""
	print(testResult)

def TestParseGPSLocation():
	testResult = ""
	print(testResult)

