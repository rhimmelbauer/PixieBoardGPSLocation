from PixieBoardGPSLocation import PixieBoardGPSLocation

def TestEnableATCommands():
	pxbdGPSLocation = PixieBoardGPSLocation()
	isEnabled, raw, error = pxbdGPSLocation.EnableATCommands()
	print("Enabled: {}\n Output: {}\n Error: {}".format(isEnabled, raw, error))
	
def TestSessionStatus():
	pxbdGPSLocation = PixieBoardGPSLocation()
	status, raw, error = pxbdGPSLocation.SessionStatus()
	print("Session Status: {}\n Output: {}\n Error: {}".format(status, raw, error))

def TestStopSession():
	pxbdGPSLocation = PixieBoardGPSLocation()
	sessionStoped, raw, error = pxbdGPSLocation.StopSession()
	print("Stopped: {}\n Output: {}\n Error: {}".format(sessionStoped, raw, error))

def TestConfigureGPSLocation():
	pxbdGPSLocation = PixieBoardGPSLocation()
	gpsConfigured, raw, error = pxbdGPSLocation.ConfigureGPSTracking()
	print("Stopped: {}\n Output: {}\n Error: {}".format(gpsConfigured, raw, error))

def TestGetGPSLocation():
	pxbdGPSLocation = PixieBoardGPSLocation()
	gotLocation, raw, error = pxbdGPSLocation.GetGPSLocation()
	print("Stopped: {}\n Output: {}\n Error: {}".format(gotLocation, raw, error))
	print("UTC Time: {}\n" \
                "Latitude: {}\n" \
                "Longitude: {}\n" \
                "HorizontalPrecision: {}\n" \
                "Altitude: {}\n" \
                "Fix: {}\n" \
                "Cog: {}\n" \
                "SpeedOverGroundKmH: {}\n" \
                "SpeedOverGroundKnots: {}\n" \
                "Date: {}\n" \
                "Number Of Satellites: {}".format(pxbdGPSLocation.UTCTime, pxbdGPSLocation.Latitude,  pxbdGPSLocation.Longitude, pxbdGPSLocation.HorizontalPrecision, pxbdGPSLocation.Altitude, pxbdGPSLocation.Fix, pxbdGPSLocation.Cog, pxbdGPSLocation.SpeedOverGroundKmH, pxbdGPSLocation.SpeedOverGroundKnots, pxbdGPSLocation.Date, pxbdGPSLocation.NumberOfSatellites)
	)

def TestGetGPSLocationPretty():
	pxbdGPSLocation = PixieBoardGPSLocation()
	gotLocation, raw, error = pxbdGPSLocation.GetGPSLocationPretty()
	print("Stopped: {}\n Output: {}\n Error: {}".format(gotLocation, raw, error))
	print("UTC Time: {}\n" \
		"Latitude: {}\n" \
		"Longitude: {}\n" \
		"HorizontalPrecision: {}\n" \
		"Altitude: {}\n" \
		"Fix: {}\n" \
		"Cog: {}\n" \
		"SpeedOverGroundKmH: {}\n" \
		"SpeedOverGroundKnots: {}\n" \
		"Date: {}\n" \
		"Number Of Satellites: {}".format(pxbdGPSLocation.UTCTime, pxbdGPSLocation.Latitude, pxbdGPSLocation.Longitude, pxbdGPSLocation.HorizontalPrecision, pxbdGPSLocation.Altitude, pxbdGPSLocation.Fix, pxbdGPSLocation.Cog, pxbdGPSLocation.SpeedOverGroundKmH, pxbdGPSLocation.SpeedOverGroundKnots, pxbdGPSLocation.Date, pxbdGPSLocation.NumberOfSatellites)
		)

def TestParseGPSLocation():
	testResult = ""
	print(testResult)

