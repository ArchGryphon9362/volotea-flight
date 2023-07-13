print("this should be illegal, but it's cool :D")
print("by arch ;)")

import requests
import time

flight_data = requests.get("https://play.volotea.com/api/flightinfo/?display_language=EN").json()
print("--- Aircraft Info ---")
print(f"Registration: {flight_data['aircraft']}")

print("--- Flight Info ---")
print(f"Flight Id: {flight_data['flight_id']}")
print(f"Origin City: {flight_data['origin_airport']['city']}")
print(f"Origin Airport: {flight_data['origin_airport']['iata_code']} - {flight_data['origin_airport']['name']}")
print(f"Origin Latitude: {flight_data['origin_airport']['latitude']}")
print(f"Origin Longitude: {flight_data['origin_airport']['latitude']}")
print(f"Destination City: {flight_data['destination_airport']['city']}")
print(f"Destination Airport: {flight_data['destination_airport']['iata_code']} - {flight_data['destination_airport']['name']}")
print(f"Destination Latitude: {flight_data['destination_airport']['latitude']}")
print(f"Destination Longitude: {flight_data['destination_airport']['latitude']}")

while True:
	print("--- New Flight Data ---")
	print(f"Latitude: {flight_data['latitude']}")
	print(f"Longitude: {flight_data['longitude']}")
	print(f"Pitch: {flight_data['pitch']}")
	print(f"Roll: {flight_data['roll']}")
	print(f"Yaw: {flight_data['yaw']}")
	print(f"Heading Angle: {flight_data['heading']}")
	print(f"Speed: Mach {flight_data['mach_speed']}")
	print(f"Ground Speed: {flight_data['ground_speed']} knots")
	print(f"Altitude: {flight_data['altitude']}ft")
	print(f"Outside Temp: {flight_data['outside_temperature']}C")
	
	time.sleep(5)
	flight_data = requests.get("https://play.volotea.com/api/flightinfo/?display_language=EN").json()
