#Python code to study Drainage line treatment Plan

import pandas as pd
import geopandas as gpd
import geemap
vector = "J:\\Project 8th sem\\REproject2\\Musakani_StreamNetwork.shp"
gdf = gpd.read_file(vector)

arcid = list(gdf["arcid"])
order = list(gdf["grid_code"])
length = list(gdf["Shape_Leng"])
froms = list(gdf["from_node"])
tos = list(gdf["to_node"])
geo = list(gdf["geometry"])


l = len(order)
strid = []
strname = []



def second(i):
    for j in range(l):
        if(froms[i]==tos[j] and order[j]==1):
            if(strid[j]==11):
                strid[i]=22
                strname[i]="LBCD"
            elif(strid[j]==12):
                strid[i]=23
                strname[i]="Gabion Structure"
            else:
                strid[i]=25
                strname[i]="Structure 5"



for i in range(l):
    strid.append(0)
    strname.append("null")

for i in range(l):
    if(order[i]==1):
        if(length[i]<=200):
            strid[i]=11
            strname[i]="Brushwood Check dam/Vegetative"
        elif(length[i]<=400):
            strid[i]=12
            strname[i]="Loose boulder check dam"
        else:
            strid[i]=13
            strname[i]="Gabion structure"

for i in range(l):
    if(order[i]>=3):
        strid[i]=30
        strname[i]="Masonary Check Dam/Earthen Check Dam"

for i in range(l):
    if(order[i]==2):
        second(i)



gdf["StructureId"] = strid
gdf["StructureName"] = strname

# gdff.to_file("Product.shp")

m = geemap.Map()
m.add_basemap()
m.add_gdf(gdf)
m
