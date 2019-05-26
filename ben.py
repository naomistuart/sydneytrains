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

# HTTPRequestHandler class
class Train(object):
    def __init__(self, latpos, longpos):
        self.latpos = latpos
        self.longpos = longpos

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
      print('hello')

      # Send response status code
      self.send_response(200)

      # Send headers
      self.send_header('Content-Type', 'application/json')
      self.end_headers()

      print('hello')

      # Send message back to client
      feed = google_gtfs_realtime_pb2.FeedMessage()
      headers = {
          'Accept': 'application/x-google-protobuf',
          'Authorization': 'apikey 6ABYMr0KI2vIVkPIKSlH9TCapL68tvdAVEvH',
      }

      response = requests.get(
          'https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/sydneytrains?debug=false', headers=headers)
      feed.ParseFromString(response._content)
      # message = feed
      # Write content as utf-8 data



      trains = []

      for entity in feed.entity:
              # crete new instance of naomi class

              # add new instance to array
          print(entity.vehicle.position.latitude)
          trains.append(Train(entity.vehicle.position.latitude,
                              entity.vehicle.position.longitude))

      print(trains)

      json_string = json.dumps(trains, default=convert_to_dict,indent=4, sort_keys=True)

      print(json_string)

      # jsons.dump(array)
      self.wfile.write(bytes(json_string.encode(encoding='utf_8')))
      # self.wfile.write(json.dumps(trains))
      return


def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', 8083)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()
