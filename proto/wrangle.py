#%%
import pandas as pd

#%%
# read in shape file
df = pd.read_excel (r'D:\personal_project\real_time_vehicle_positions\SydneyTrainsGTFS_TransitBundle_28thApr\master_routes_stops.xlsx', sheet_name="shapes")

#%%
# create master longlats
# data structure = [[[], [], ..., []], ..., [[], [], ..., []]]
# smallest layer = [long, lat]
# middle layer = [long, lat]s for one route
# top layer = combining all routes
route_lookup = {'NSN_1a': 'T1', 'NSN_2a': 'T1', 'NSN_2i': 'T1', 'NSN_2k': 'T1', 'WST_1a': 'T1', 'WST_1b': 'T1', 'WST_2c': 'T1', 'WST_2d': 'T1', 'IWL_1a': 'T2', 'IWL_1b': 'T2', 'IWL_1c': 'T2', 'IWL_1d': 'T2', 'BMT_1': 'BMT', 'BMT_2': 'BMT', 'IWL_1e': 'T2', 'IWL_1f': 'T2', 'IWL_1g': 'T2', 'IWL_1h': 'T2', 'IWL_1i': 'T2', 'IWL_1j': 'T2', 'IWL_2a': 'T2', 'IWL_2b': 'T2', 'IWL_2c': 'T2', 'IWL_2d': 'T2', 'IWL_2e': 'T2', 'IWL_2f': 'T2', 'IWL_2g': 'T2', 'IWL_2h': 'T2', 'IWL_2i': 'T2', 'IWL_2j': 'T2', 'CCN_1a': 'CCN', 'CCN_1b': 'CCN', 'CCN_1c': 'CCN', 'CCN_2a': 'CCN', 'CCN_2b': 'CCN', 'BNK_1a': 'T3', 'BNK_1b': 'T3', 'BNK_1c': 'T3', 'BNK_1d': 'T3', 'BNK_1e': 'T3', 'BNK_1f': 'T3', 'BNK_1g': 'T3', 'BNK_1h': 'T3', 'BNK_2a': 'T3', 'BNK_2b': 'T3', 'CTY_NC1': 'NRC', 'CTY_NC1a': 'NRC', 'CTY_NC2': 'NRC', 'CTY_NW1a': 'NRW', 'CTY_NW1b': 'NRW', 'CTY_NW1c': 'NRW', 'CTY_NW1d': 'NRW', 'CTY_NW2a': 'NRW', 'CTY_NW2b': 'NRW', 'CTY_S1a': 'STH', 'CTY_S1b': 'STH', 'CTY_S1c': 'STH', 'CTY_S1d': 'STH', 'CTY_S1e': 'STH', 'CTY_S1f': 'STH', 'CTY_S1g': 'STH', 'CTY_S1h': 'STH', 'CTY_S1i': 'STH', 'CTY_S2a': 'STH', 'CTY_S2b': 'STH', 'CTY_S2c': 'STH', 'CTY_S2d': 'STH', 'CTY_S2e': 'STH', 'CTY_S2f': 'STH', 'CTY_S2g': 'STH', 'CTY_S2h': 'STH', 'CTY_S2i': 'STH', 'CTY_W1a': 'WST', 'CTY_W1b': 'WST', 'CTY_W2a': 'WST', 'CTY_W2b': 'WST', 'BNK_2c': 'T3', 'BNK_2d': 'T3', 'BNK_2e': 'T3', 'BNK_2f': 'T3', 'BNK_2g': 'T3', 'BNK_2h': 'T3', 'ESI_1a': 'T4', 'ESI_1b': 'T4', 'ESI_1c': 'T4', 'ESI_1d': 'T4', 'ESI_1e': 'T4', 'ESI_1f': 'T4', 'HUN_1a': 'HUN', 'HUN_1b': 'HUN', 'HUN_2a': 'HUN', 'HUN_2b': 'HUN', 'ESI_2a': 'T4', 'ESI_2b': 'T4', 'ESI_2c': 'T4', 'ESI_2d': 'T4', 'ESI_2e': 'T4', 'ESI_2f': 'T4', 'CMB_1a': 'T5', 'CMB_1b': 'T5', 'CMB_1c': 'T5', 'CMB_1d': 'T5', 'CMB_2a': 'T5', 'CMB_2b': 'T5', 'CMB_2c': 'T5', 'CMB_2d': 'T5', 'CGF_1': 'T6', 'CGF_2': 'T6', 'OLY_1a': 'T7', 'OLY_1b': 'T7', 'OLY_2a': 'T7', 'OLY_2b': 'T7', 'APS_1a': 'T8', 'APS_1b': 'T8', 'APS_1c': 'T8', 'APS_1d': 'T8', 'APS_1e': 'T8', 'APS_1f': 'T8', 'APS_2a': 'T8', 'APS_2b': 'T8', 'APS_2c': 'T8', 'APS_2d': 'T8', 'APS_2e': 'T8', 'RTTA_DEF': 'other', 'RTTA_REV': 'other', 'SCO_1a': 'SCO', 'SCO_1b': 'SCO', 'SCO_2a': 'SCO', 'SCO_2b': 'SCO', 'SHL_1a': 'SHL', 'SHL_1b': 'SHL', 'SHL_1c': 'SHL', 'SHL_1d': 'SHL', 'SHL_1e': 'SHL', 'SHL_2a': 'SHL', 'SHL_2b': 'SHL', 'SHL_2c': 'SHL', 'SHL_2d': 'SHL', 'SHL_2e': 'SHL', 'APS_2f': 'T8', 'NTH_1a': 'T9', 'NTH_1b': 'T9', 'NTH_2a': 'T9'}
longlats = []
for key, value in route_lookup.items():
    df_route = df.loc[df['shape_id'] == key]
    route_longlats = []
    for index, row in df_route.iterrows():
        route_longlats.append([row['shape_pt_lon'], row['shape_pt_lat']])
    longlats.append(route_longlats)

print(longlats)

#%%
# colors = pd.read_excel (r'D:\personal_project\real_time_vehicle_positions\SydneyTrainsGTFS_TransitBundle_28thApr\master_routes_stops.xlsx', sheet_name="colours")
# color_lookup = dict(zip(colors['route_short'], colors['route_color']))
# for key, value in color_lookup.items():
#     color_lookup[key] = '#' + str(value)

# print(color_lookup)

color_lookup = {'T1': '#F99D1C', 'T2': '#0098CD', 'T3': '#F37021', 'T4': '#005AA3', 'T5': '#C4258F', 'T6': '#456CAA', 'T7': '#6F818E', 'T8': '#00954C', 'T9': '#D11F2F', 'BMT': '#F99D1C', 'CCN': '#D11F2F', 'NRC': '#F6891F', 'NRW': '#F6891F', 'STH': '#F6891F', 'WST': '#F6891F', 'HUN': '#833134', 'other': '#888888', 'SCO': '#005AA3', 'SHL': '#00954C'}

    
#%%
t4_df = df.loc[df['shape_id'] == 'ESI_1d']
#print(t4_df)


#Route_id LookUp
#route_lookup = {'NSN_1a': 'T1', 'NSN_2a': 'T1', 'NSN_2i': 'T1', 'NSN_2k': 'T1', 'WST_1a': 'T1', 'WST_1b': 'T1', 'WST_2c': 'T1', 'WST_2d': 'T1', 'IWL_1a': 'T2', 'IWL_1b': 'T2', 'IWL_1c': 'T2', 'IWL_1d': 'T2', 'BMT_1': 'BMT', 'BMT_2': 'BMT', 'IWL_1e': 'T2', 'IWL_1f': 'T2', 'IWL_1g': 'T2', 'IWL_1h': 'T2', 'IWL_1i': 'T2', 'IWL_1j': 'T2', 'IWL_2a': 'T2', 'IWL_2b': 'T2', 'IWL_2c': 'T2', 'IWL_2d': 'T2', 'IWL_2e': 'T2', 'IWL_2f': 'T2', 'IWL_2g': 'T2', 'IWL_2h': 'T2', 'IWL_2i': 'T2', 'IWL_2j': 'T2', 'CCN_1a': 'CCN', 'CCN_1b': 'CCN', 'CCN_1c': 'CCN', 'CCN_2a': 'CCN', 'CCN_2b': 'CCN', 'BNK_1a': 'T3', 'BNK_1b': 'T3', 'BNK_1c': 'T3', 'BNK_1d': 'T3', 'BNK_1e': 'T3', 'BNK_1f': 'T3', 'BNK_1g': 'T3', 'BNK_1h': 'T3', 'BNK_2a': 'T3', 'BNK_2b': 'T3', 'CTY_NC1': 'NRC', 'CTY_NC1a': 'NRC', 'CTY_NC2': 'NRC', 'CTY_NW1a': 'NRW', 'CTY_NW1b': 'NRW', 'CTY_NW1c': 'NRW', 'CTY_NW1d': 'NRW', 'CTY_NW2a': 'NRW', 'CTY_NW2b': 'NRW', 'CTY_S1a': 'STH', 'CTY_S1b': 'STH', 'CTY_S1c': 'STH', 'CTY_S1d': 'STH', 'CTY_S1e': 'STH', 'CTY_S1f': 'STH', 'CTY_S1g': 'STH', 'CTY_S1h': 'STH', 'CTY_S1i': 'STH', 'CTY_S2a': 'STH', 'CTY_S2b': 'STH', 'CTY_S2c': 'STH', 'CTY_S2d': 'STH', 'CTY_S2e': 'STH', 'CTY_S2f': 'STH', 'CTY_S2g': 'STH', 'CTY_S2h': 'STH', 'CTY_S2i': 'STH', 'CTY_W1a': 'WST', 'CTY_W1b': 'WST', 'CTY_W2a': 'WST', 'CTY_W2b': 'WST', 'BNK_2c': 'T3', 'BNK_2d': 'T3', 'BNK_2e': 'T3', 'BNK_2f': 'T3', 'BNK_2g': 'T3', 'BNK_2h': 'T3', 'ESI_1a': 'T4', 'ESI_1b': 'T4', 'ESI_1c': 'T4', 'ESI_1d': 'T4', 'ESI_1e': 'T4', 'ESI_1f': 'T4', 'HUN_1a': 'HUN', 'HUN_1b': 'HUN', 'HUN_2a': 'HUN', 'HUN_2b': 'HUN', 'ESI_2a': 'T4', 'ESI_2b': 'T4', 'ESI_2c': 'T4', 'ESI_2d': 'T4', 'ESI_2e': 'T4', 'ESI_2f': 'T4', 'CMB_1a': 'T5', 'CMB_1b': 'T5', 'CMB_1c': 'T5', 'CMB_1d': 'T5', 'CMB_2a': 'T5', 'CMB_2b': 'T5', 'CMB_2c': 'T5', 'CMB_2d': 'T5', 'CGF_1': 'T6', 'CGF_2': 'T6', 'OLY_1a': 'T7', 'OLY_1b': 'T7', 'OLY_2a': 'T7', 'OLY_2b': 'T7', 'APS_1a': 'T8', 'APS_1b': 'T8', 'APS_1c': 'T8', 'APS_1d': 'T8', 'APS_1e': 'T8', 'APS_1f': 'T8', 'APS_2a': 'T8', 'APS_2b': 'T8', 'APS_2c': 'T8', 'APS_2d': 'T8', 'APS_2e': 'T8', 'RTTA_DEF': 'other', 'RTTA_REV': 'other', 'SCO_1a': 'SCO', 'SCO_1b': 'SCO', 'SCO_2a': 'SCO', 'SCO_2b': 'SCO', 'SHL_1a': 'SHL', 'SHL_1b': 'SHL', 'SHL_1c': 'SHL', 'SHL_1d': 'SHL', 'SHL_1e': 'SHL', 'SHL_2a': 'SHL', 'SHL_2b': 'SHL', 'SHL_2c': 'SHL', 'SHL_2d': 'SHL', 'SHL_2e': 'SHL', 'APS_2f': 'T8', 'NTH_1a': 'T9', 'NTH_1b': 'T9', 'NTH_2a': 'T9'}

t4_longlat = []
for index, row in t4_df.iterrows():
    t4_longlat.append([row['shape_pt_lon'], row['shape_pt_lat']])
print(t4_longlat)
    