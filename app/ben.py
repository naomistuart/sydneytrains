# -*- coding: utf-8 -*-
"""
Created on Sun May  5 16:26:24 2019

@author: naomi
"""

#!/usr/bin/env python
 
from http.server import BaseHTTPRequestHandler, HTTPServer
import google_gtfs_realtime_pb2
import requests
import json
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        feed = google_gtfs_realtime_pb2.FeedMessage()
        headers = {
          'Accept': 'application/x-google-protobuf',
          'Authorization': 'apikey 6ABYMr0KI2vIVkPIKSlH9TCapL68tvdAVEvH',
        }

        response = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/sydneytrains?debug=false', headers=headers)
        feed.ParseFromString(response._content)
        # message = feed
        # Write content as utf-8 data
        for entity in feed.entity:

          # crete new instance of naomi class

          # add new instance to array

        # jsons.dump(array)
        self.wfile.write(json.dumps(entity.vehicle.trip))
        return
 
def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
 
run()