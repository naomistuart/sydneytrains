#!/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import os
import cgi
import google_gtfs_realtime_pb2
import requests
import json


route_lookup = {'NSN_1a': 'T1', 'NSN_2a': 'T1', 'NSN_2i': 'T1', 'NSN_2k': 'T1', 'WST_1a': 'T1', 'WST_1b': 'T1', 'WST_2c': 'T1', 'WST_2d': 'T1', 'IWL_1a': 'T2', 'IWL_1b': 'T2', 'IWL_1c': 'T2', 'IWL_1d': 'T2', 'BMT_1': 'BMT', 'BMT_2': 'BMT', 'IWL_1e': 'T2', 'IWL_1f': 'T2', 'IWL_1g': 'T2', 'IWL_1h': 'T2', 'IWL_1i': 'T2', 'IWL_1j': 'T2', 'IWL_2a': 'T2', 'IWL_2b': 'T2', 'IWL_2c': 'T2', 'IWL_2d': 'T2', 'IWL_2e': 'T2', 'IWL_2f': 'T2', 'IWL_2g': 'T2', 'IWL_2h': 'T2', 'IWL_2i': 'T2', 'IWL_2j': 'T2', 'CCN_1a': 'CCN', 'CCN_1b': 'CCN', 'CCN_1c': 'CCN', 'CCN_2a': 'CCN', 'CCN_2b': 'CCN', 'BNK_1a': 'T3', 'BNK_1b': 'T3', 'BNK_1c': 'T3', 'BNK_1d': 'T3', 'BNK_1e': 'T3', 'BNK_1f': 'T3', 'BNK_1g': 'T3', 'BNK_1h': 'T3', 'BNK_2a': 'T3', 'BNK_2b': 'T3', 'CTY_NC1': 'NRC', 'CTY_NC1a': 'NRC', 'CTY_NC2': 'NRC', 'CTY_NW1a': 'NRW', 'CTY_NW1b': 'NRW', 'CTY_NW1c': 'NRW', 'CTY_NW1d': 'NRW', 'CTY_NW2a': 'NRW', 'CTY_NW2b': 'NRW', 'CTY_S1a': 'STH', 'CTY_S1b': 'STH', 'CTY_S1c': 'STH', 'CTY_S1d': 'STH', 'CTY_S1e': 'STH', 'CTY_S1f': 'STH', 'CTY_S1g': 'STH', 'CTY_S1h': 'STH', 'CTY_S1i': 'STH', 'CTY_S2a': 'STH', 'CTY_S2b': 'STH', 'CTY_S2c': 'STH', 'CTY_S2d': 'STH', 'CTY_S2e': 'STH', 'CTY_S2f': 'STH', 'CTY_S2g': 'STH', 'CTY_S2h': 'STH', 'CTY_S2i': 'STH', 'CTY_W1a': 'WST', 'CTY_W1b': 'WST', 'CTY_W2a': 'WST', 'CTY_W2b': 'WST', 'BNK_2c': 'T3', 'BNK_2d': 'T3', 'BNK_2e': 'T3', 'BNK_2f': 'T3', 'BNK_2g': 'T3', 'BNK_2h': 'T3', 'ESI_1a': 'T4', 'ESI_1b': 'T4', 'ESI_1c': 'T4', 'ESI_1d': 'T4', 'ESI_1e': 'T4', 'ESI_1f': 'T4', 'HUN_1a': 'HUN', 'HUN_1b': 'HUN', 'HUN_2a': 'HUN', 'HUN_2b': 'HUN', 'ESI_2a': 'T4', 'ESI_2b': 'T4', 'ESI_2c': 'T4', 'ESI_2d': 'T4', 'ESI_2e': 'T4', 'ESI_2f': 'T4', 'CMB_1a': 'T5', 'CMB_1b': 'T5', 'CMB_1c': 'T5', 'CMB_1d': 'T5', 'CMB_2a': 'T5', 'CMB_2b': 'T5', 'CMB_2c': 'T5', 'CMB_2d': 'T5', 'CGF_1': 'T6', 'CGF_2': 'T6', 'OLY_1a': 'T7', 'OLY_1b': 'T7', 'OLY_2a': 'T7', 'OLY_2b': 'T7', 'APS_1a': 'T8', 'APS_1b': 'T8', 'APS_1c': 'T8', 'APS_1d': 'T8', 'APS_1e': 'T8', 'APS_1f': 'T8', 'APS_2a': 'T8', 'APS_2b': 'T8', 'APS_2c': 'T8', 'APS_2d': 'T8', 'APS_2e': 'T8', 'RTTA_DEF': 'other', 'RTTA_REV': 'other', 'SCO_1a': 'SCO', 'SCO_1b': 'SCO', 'SCO_2a': 'SCO', 'SCO_2b': 'SCO', 'SHL_1a': 'SHL', 'SHL_1b': 'SHL', 'SHL_1c': 'SHL', 'SHL_1d': 'SHL', 'SHL_1e': 'SHL', 'SHL_2a': 'SHL', 'SHL_2b': 'SHL', 'SHL_2c': 'SHL', 'SHL_2d': 'SHL', 'SHL_2e': 'SHL', 'APS_2f': 'T8', 'NTH_1a': 'T9', 'NTH_1b': 'T9', 'NTH_2a': 'T9'}
color_lookup = {'T1': '#F99D1C', 'T2': '#0098CD', 'T3': '#F37021', 'T4': '#005AA3', 'T5': '#C4258F', 'T6': '#456CAA', 'T7': '#6F818E', 'T8': '#00954C', 'T9': '#D11F2F', 'BMT': '#F99D1C', 'CCN': '#D11F2F', 'NRC': '#F6891F', 'NRW': '#F6891F', 'STH': '#F6891F', 'WST': '#F6891F', 'HUN': '#833134', 'other': '#888888', 'SCO': '#005AA3', 'SHL': '#00954C'}

# find nth occurence of substring in string
def findnth(string, substring, n):
    parts = string.split(substring, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(string) - len(parts[-1]) - len(substring)

class Train(object):
	def __init__(self, latpos, longpos, route, display, trainset, numcars, color):
		self.latpos = latpos
		self.longpos = longpos
		self.route = route
		self.display = display
		self.trainset = trainset
		self.numcars = numcars
		self.color = color

def convert_to_dict(obj):
  """
  A function takes in a custom object and returns a dictionary representation of the object.
  This dict representation includes meta data such as the object's module and class names.
  """
  
  #  Populate the dictionary with object meta data 
  obj_dict = {}
  
  #  Populate the dictionary with object properties
  obj_dict.update(obj.__dict__)
  
  return obj_dict

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):

		if self.path=="/trains":
			#Get NSW data
			feed = google_gtfs_realtime_pb2.FeedMessage()
			headers = {
				'Accept': 'application/x-google-protobuf',
				'Authorization': 'apikey 6ABYMr0KI2vIVkPIKSlH9TCapL68tvdAVEvH',
			}
			response = requests.get(
				'https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/sydneytrains?debug=false', headers=headers)
			feed.ParseFromString(response._content)

			trains = []

			for entity in feed.entity:
				if entity.vehicle.trip.route_id != "":
					trip_id = entity.vehicle.trip.trip_id
					trains.append(Train(entity.vehicle.position.latitude, entity.vehicle.position.longitude, route_lookup[entity.vehicle.trip.route_id], entity.vehicle.vehicle.label, trip_id[findnth(trip_id, ".", 3)+1], trip_id[findnth(trip_id, ".", 4)+1], color_lookup[route_lookup[entity.vehicle.trip.route_id]]))

			json_string = json.dumps(trains, default=convert_to_dict,indent=4, sort_keys=True)

			# Send response status code
			self.send_response(200)

			# Send headers
			self.send_header('Content-Type', 'application/json')
			self.end_headers()

			self.wfile.write(bytes(json_string.encode(encoding='utf_8')))
			return

		if self.path=="/":
			self.path="/index.html"

		try:
			#Check the file extension required and
			#set the right mime type

			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith(".jpg"):
				mimetype='image/jpg'
				sendReply = True
			if self.path.endswith(".png"):
				mimetype='image/png'
				f = open(curdir + sep + self.path, 'rb') 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
				return
			if self.path.endswith(".js"):
				mimetype='application/javascript'
				sendReply = True
			if self.path.endswith(".css"):
				mimetype='text/css'
				sendReply = True

			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path) 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(bytes(f.read(), 'utf8'))
				f.close()
			return

		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)	
			
			
try:
	#Create a web server and define the handler to manage the
	#incoming request
	PORT_NUMBER = int(os.environ.get('PORT', 8080))
	print("hello")
	print(os.environ)
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print('Started httpserver on port ', PORT_NUMBER) 
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')
	server.socket.close()