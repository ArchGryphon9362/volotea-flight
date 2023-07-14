print("this should be illegal, but it's cool :D")
print("by arch ;)")

import requests
import time

flight_data = requests.get("https://play.volotea.com/api/flightinfo/?display_language=EN").json()
print(f"""--- Aircraft Info ---
Registration: {flight_data['aircraft']}""")

print(f"""--- Flight Info ---
Flight Id: {flight_data['flight_id']}
Origin City: {flight_data['origin_airport']['city']}
Origin Airport: {flight_data['origin_airport']['iata_code']} - {flight_data['origin_airport']['name']}
Origin Latitude: {flight_data['origin_airport']['latitude']}
Origin Longitude: {flight_data['origin_airport']['longitude']}
Destination City: {flight_data['destination_airport']['city']}
Destination Airport: {flight_data['destination_airport']['iata_code']} - {flight_data['destination_airport']['name']}")
Destination Latitude: {flight_data['destination_airport']['latitude']}
Destination Longitude: {flight_data['destination_airport']['longitude']}""")

while True:
	print(f"""--- New Flight Data ---
Latitude: {flight_data['latitude']}
Longitude: {flight_data['longitude']}
Pitch: {flight_data['pitch']}
Roll: {flight_data['roll']}
Yaw: {flight_data['yaw']}
Heading Angle: {flight_data['heading']}
Speed: Mach {flight_data['mach_speed']}
Ground Speed: {flight_data['ground_speed']} knots
Altitude: {flight_data['altitude']}ft
Outside Temp: {flight_data['outside_temperature']}C""")
	time.sleep(5)
	flight_data = requests.get("https://play.volotea.com/api/flightinfo/?display_language=EN").json()
