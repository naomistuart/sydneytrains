
import pandas as pd

# read in shape file
shapes = pd.read_excel (r'C:\dev\repos\sydneytrains\SydneyTrainsGTFS_TransitBundle_28thApr\master_routes_stops.xlsx', sheetname='shapes')
routes = pd.read_excel (r'C:\dev\repos\sydneytrains\SydneyTrainsGTFS_TransitBundle_28thApr\master_routes_stops.xlsx', sheetname='master_routes')



# Prints out coordinates of train line given route code
#def getTrainLineCoordinates(trainLine, shapes):
#    df_trainLine = shapes.loc[shapes['shape_id'] == trainLine]
#    longlats = []
#    for index, row in df_trainLine.iterrows():
#        longlats.append([row['shape_pt_lon'], row['shape_pt_lat']])
#    print(longlats)

# Creates JSON of polylines
# Initialise file
f = open(r'C:\dev\repos\sydneytrains\app\trainpaths.js', 'w')
f.write("map.on('load', function () {\n")

# Access colour and latlat info from dataframe
for route in routes['route_id']:
    colour = pd.Series.to_string(routes.loc[routes['route_id'] == route, 'colour'])[-6:]
    df_route = shapes.loc[shapes['shape_id'] == route]
    longlats = []
    for index, row in df_route.iterrows():
        longlats.append([row['shape_pt_lon'], row['shape_pt_lat']])
        
    # Write to JavaScript file
    f.write('map.addLayer({\n')
    f.write('"id": ' + '"' + str(route) + '"' +',\n')
    f.write('"type": "line",\n')
    f.write('"source": {\n')
    f.write('"type": "geojson",\n')
    f.write('"data": {\n')
    f.write('"type": "Feature",\n')
    f.write('"properties": {},\n')
    f.write('"geometry": {\n')
    f.write('"type": "LineString",\n')
    f.write('"coordinates": '+ str(longlats) + '\n')
    f.write('}\n')
    f.write('}\n')
    f.write('},\n')
    f.write('"layout": {\n')
    f.write('"line-join": "round",\n')
    f.write('"line-cap": "round"\n')
    f.write('},\n')
    f.write('"paint": {\n')
    f.write('"line-color": '+ '\"#' + str(colour) + '\"' + ',\n')
    f.write('"line-width": 3\n')
    f.write('}\n')
    f.write('});\n')
    f.write('\n')
    
f.write("});\n")
f.close()
