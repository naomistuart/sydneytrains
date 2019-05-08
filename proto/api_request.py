#
##google
#feed = gtfs_realtime_pb2.FeedMessage()
#response = urllib.urlopen('URL OF YOUR GTFS-REALTIME SOURCE GOES HERE')
#feed.ParseFromString(response.read())
#for entity in feed.entity:
#  if entity.HasField('trip_update'):
#    print(entity.trip_update)
#    
#    
##mine
#import requests
#
#headers = {
#    'Accept': 'application/x-google-protobuf',
#    'Authorization': 'apikey 6ABYMr0KI2vIVkPIKSlH9TCapL68tvdAVEvH',
#}
#
#response = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/sydneytrains?debug=false', headers=headers)
#response.encoding = 'utf-8'
#print(response.text)

##sample code
#for entity in feed.entity:
#    if entity.vehicle.trip.route_id=="":
#        print(entity.vehicle.trip)

#print(response._content)
#      if entity.HasField('vehicle'):
#    print(entity.vehicle)


#new
import google_gtfs_realtime_pb2
import requests

feed = google_gtfs_realtime_pb2.FeedMessage()
headers = {
    'Accept': 'application/x-google-protobuf',
    'Authorization': 'apikey 6ABYMr0KI2vIVkPIKSlH9TCapL68tvdAVEvH',
}

response = requests.get('https://api.transport.nsw.gov.au/v1/gtfs/vehiclepos/sydneytrains?debug=false', headers=headers)
feed.ParseFromString(response._content)
#for entity in feed.entity:
#    if entity.vehicle.trip.route_id=="":
#        print(entity.vehicle.trip)
route_lookup = {'NSN_1a': 'T1', 'NSN_2a': 'T1', 'NSN_2i': 'T1', 'NSN_2k': 'T1', 'WST_1a': 'T1', 'WST_1b': 'T1', 'WST_2c': 'T1', 'WST_2d': 'T1', 'IWL_1a': 'T2', 'IWL_1b': 'T2', 'IWL_1c': 'T2', 'IWL_1d': 'T2', 'BMT_1': 'BMT', 'BMT_2': 'BMT', 'IWL_1e': 'T2', 'IWL_1f': 'T2', 'IWL_1g': 'T2', 'IWL_1h': 'T2', 'IWL_1i': 'T2', 'IWL_1j': 'T2', 'IWL_2a': 'T2', 'IWL_2b': 'T2', 'IWL_2c': 'T2', 'IWL_2d': 'T2', 'IWL_2e': 'T2', 'IWL_2f': 'T2', 'IWL_2g': 'T2', 'IWL_2h': 'T2', 'IWL_2i': 'T2', 'IWL_2j': 'T2', 'CCN_1a': 'CCN', 'CCN_1b': 'CCN', 'CCN_1c': 'CCN', 'CCN_2a': 'CCN', 'CCN_2b': 'CCN', 'BNK_1a': 'T3', 'BNK_1b': 'T3', 'BNK_1c': 'T3', 'BNK_1d': 'T3', 'BNK_1e': 'T3', 'BNK_1f': 'T3', 'BNK_1g': 'T3', 'BNK_1h': 'T3', 'BNK_2a': 'T3', 'BNK_2b': 'T3', 'CTY_NC1': 'NRC', 'CTY_NC1a': 'NRC', 'CTY_NC2': 'NRC', 'CTY_NW1a': 'NRW', 'CTY_NW1b': 'NRW', 'CTY_NW1c': 'NRW', 'CTY_NW1d': 'NRW', 'CTY_NW2a': 'NRW', 'CTY_NW2b': 'NRW', 'CTY_S1a': 'STH', 'CTY_S1b': 'STH', 'CTY_S1c': 'STH', 'CTY_S1d': 'STH', 'CTY_S1e': 'STH', 'CTY_S1f': 'STH', 'CTY_S1g': 'STH', 'CTY_S1h': 'STH', 'CTY_S1i': 'STH', 'CTY_S2a': 'STH', 'CTY_S2b': 'STH', 'CTY_S2c': 'STH', 'CTY_S2d': 'STH', 'CTY_S2e': 'STH', 'CTY_S2f': 'STH', 'CTY_S2g': 'STH', 'CTY_S2h': 'STH', 'CTY_S2i': 'STH', 'CTY_W1a': 'WST', 'CTY_W1b': 'WST', 'CTY_W2a': 'WST', 'CTY_W2b': 'WST', 'BNK_2c': 'T3', 'BNK_2d': 'T3', 'BNK_2e': 'T3', 'BNK_2f': 'T3', 'BNK_2g': 'T3', 'BNK_2h': 'T3', 'ESI_1a': 'T4', 'ESI_1b': 'T4', 'ESI_1c': 'T4', 'ESI_1d': 'T4', 'ESI_1e': 'T4', 'ESI_1f': 'T4', 'HUN_1a': 'HUN', 'HUN_1b': 'HUN', 'HUN_2a': 'HUN', 'HUN_2b': 'HUN', 'ESI_2a': 'T4', 'ESI_2b': 'T4', 'ESI_2c': 'T4', 'ESI_2d': 'T4', 'ESI_2e': 'T4', 'ESI_2f': 'T4', 'CMB_1a': 'T5', 'CMB_1b': 'T5', 'CMB_1c': 'T5', 'CMB_1d': 'T5', 'CMB_2a': 'T5', 'CMB_2b': 'T5', 'CMB_2c': 'T5', 'CMB_2d': 'T5', 'CGF_1': 'T6', 'CGF_2': 'T6', 'OLY_1a': 'T7', 'OLY_1b': 'T7', 'OLY_2a': 'T7', 'OLY_2b': 'T7', 'APS_1a': 'T8', 'APS_1b': 'T8', 'APS_1c': 'T8', 'APS_1d': 'T8', 'APS_1e': 'T8', 'APS_1f': 'T8', 'APS_2a': 'T8', 'APS_2b': 'T8', 'APS_2c': 'T8', 'APS_2d': 'T8', 'APS_2e': 'T8', 'RTTA_DEF': 'other', 'RTTA_REV': 'other', 'SCO_1a': 'SCO', 'SCO_1b': 'SCO', 'SCO_2a': 'SCO', 'SCO_2b': 'SCO', 'SHL_1a': 'SHL', 'SHL_1b': 'SHL', 'SHL_1c': 'SHL', 'SHL_1d': 'SHL', 'SHL_1e': 'SHL', 'SHL_2a': 'SHL', 'SHL_2b': 'SHL', 'SHL_2c': 'SHL', 'SHL_2d': 'SHL', 'SHL_2e': 'SHL', 'APS_2f': 'T8', 'NTH_1a': 'T9', 'NTH_1b': 'T9', 'NTH_2a': 'T9'}
images_lookup = {'T1': 'T1.png', 'T2': 'T2.png', 'T3': 'T3.png', 'T4': 'T4.png', 'T5': 'T5.png', 'T6': 'T6.png', 'T7': 'T7.png', 'T8': 'T8.png', 'T9': 'T9.png', 'BMT': 'BMT.png', 'CCN': 'CCN.png', 'NRC': 'NRC.png', 'NRW': 'NRW.png', 'STH': 'STH.png', 'WST': 'WST.png', 'HUN': 'HUN.png', 'SCO': 'SCO.png', 'SHL': 'SHL.png'}
routes = []
latitudes = []
longitudes = []
for entity in feed.entity:
    if entity.vehicle.trip.route_id != "":
        routes.append(route_lookup[entity.vehicle.trip.route_id])
        latitudes.append(entity.vehicle.position.latitude)
        longitudes.append(entity.vehicle.position.longitude)
        
#print(routes)
#print(latitudes)
#print(longitudes)

#print(response._content)
#      if entity.HasField('vehicle'):
#    print(entity.vehicle)
        
numTrains = 0
for entity in feed.entity:
    if entity.vehicle.trip.route_id != "":
        numTrains += 1

currentTrain = 1

f = open(r'C:\dev\repos\sydneytrains\app\geojson.js', 'w')
f.write("var geojson = {\n")
f.write("type: 'FeatureCollection',\n")
f.write("features: [\n")
for entity in feed.entity:
    if entity.vehicle.trip.route_id != "":
        f.write("{\n")
        f.write("type: 'Feature',\n")
        f.write("geometry: {\n")
        f.write("type: 'Point',\n")
        #f.write("coordinates: [" + str(round(entity.vehicle.position.longitude, 4)) + ", " + str(round(entity.vehicle.position.latitude, 4)) + "]\n")
        f.write("coordinates: [" + str(entity.vehicle.position.longitude) + ", " + str(entity.vehicle.position.latitude) + "]\n")
        f.write("},\n")
        f.write("properties: {\n")
        f.write("title: 'Mapbox',\n")
        #f.write("trainline: \'" + str(route_lookup[entity.vehicle.trip.route_id]) + "\'\n")
        #f.write("trainline: \'icons/T1.png'\n")
        f.write("trainline: \'icons/" + str(images_lookup.get(route_lookup[entity.vehicle.trip.route_id], "other.png")) + "\'\n")
        f.write("}\n")
        if currentTrain == numTrains:
            f.write("}]\n")
        else:
            f.write("},\n")
        currentTrain += 1
f.write("};\n")
f.close()

#print("var geojson = {")
#print("type: 'FeatureCollection',")
#print("features: [")
#for entity in feed.entity:
#    if entity.vehicle.trip.route_id != "":
#        print("{")
#        print("type: 'Feature',")
#        print("geometry: {")
#        print("type: 'Point',")
#        print("coordinates: [" + str(round(entity.vehicle.position.longitude, 2)) + ", " + str(round(entity.vehicle.position.latitude, 2)) + "]")
#        print("},")
#        print("properties: {")
#        print("title: 'Mapbox',")
#        print("trainline: \'" + str(route_lookup[entity.vehicle.trip.route_id]) + "\'")
#        print("}")
#        if currentTrain == numTrains:
#            print("}]")
#        else:
#            print("},")
#        currentTrain += 1
#print("};")
