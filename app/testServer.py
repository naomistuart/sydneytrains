#!/usr/bin/python
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import cgi
import google_gtfs_realtime_pb2
import requests
import json

PORT_NUMBER = 8080

class Train(object):
	def __init__(self, latpos, longpos):
		self.latpos = latpos
		self.longpos = longpos

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
				trains.append(Train(entity.vehicle.position.latitude,
									entity.vehicle.position.longitude))

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
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print('Started httpserver on port ', PORT_NUMBER) 
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')
	server.socket.close()