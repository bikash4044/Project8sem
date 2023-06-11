#python code to study Soil Conservation Structure

import geopandas as gpd
import pandas as pd
import leafmap as lf
import geemap
#read the shapefile
vector = "J:\\Project 8th sem\\Musakani_Soil_phase\\musakani_scp.shp"
gdf = gpd.read_file(vector)
            
vector2 = "J:\\Project 8th sem\\Musakani MWS\\Musakani_MWS.shp"
gdf02 = gpd.read_file(vector2)

#classify the table to create tables for each structure
gdf1 = gdf[(gdf['LULC'] != 'Arable land') & ((gdf['New_Slope'] == "Moderately steeply sloping (10-15 %)") | (gdf['New_Slope'] == "Steeply sloping (15-25 %)") ) & ((gdf['Soil_Depth'] == "Shallow (25-50 cm)")|(gdf['Soil_Depth'] == "Moderately deep (75-100 cm)")|(gdf['Soil_Depth'] == "Deep (100-150 cm)")) ] #staggerd trench >25
gdf2 = gdf[(gdf['LULC'] != 'Arable land') & ((gdf['New_Slope'] == "Moderately steeply sloping (10-15 %)") | (gdf['New_Slope'] == "Steeply sloping (15-25 %)") ) & ((gdf['Soil_Depth'] != "Shallow (25-50 cm)")&(gdf['Soil_Depth'] != "Moderately deep (75-100 cm)")&(gdf['Soil_Depth'] != "Deep (100-150 cm)")) ] #Trench cum bund <25
gdf3 = gdf[(gdf['LULC'] != 'Arable land') & ((gdf['New_Slope'] == "Very gently sloping (1-3%)") | (gdf['New_Slope'] == "Gently sloping (3-5%)") | (gdf['New_Slope'] == "Moderately sloping (5-10%)")) & ((gdf['Soil_Depth'] == "Shallow (25-50 cm)")|(gdf['Soil_Depth'] == "Moderately deep (75-100 cm)")|(gdf['Soil_Depth'] == "Deep (100-150 cm)")) ] #stonebunding1 >25
gdf4 = gdf[(gdf['LULC'] != 'Arable land') & ((gdf['New_Slope'] == "Very gently sloping (1-3%)") | (gdf['New_Slope'] == "Gently sloping (3-5%)") | (gdf['New_Slope'] == "Moderately sloping (5-10%)")) & ((gdf['Soil_Depth'] != "Shallow (25-50 cm)")&(gdf['Soil_Depth'] != "Moderately deep (75-100 cm)")&(gdf['Soil_Depth'] != "Deep (100-150 cm)")) ] #stonebunding2 <25
gdf5 = gdf[(gdf['LULC'] == 'Arable land') & ((gdf['New_Slope'] == "Moderately steeply sloping (10-15 %)") | (gdf['New_Slope'] == "Steeply sloping (15-25 %)"))] #Terrace
gdf6 = gdf[(gdf['LULC'] == 'Arable land') & ((gdf['New_Slope'] == "Moderately sloping (5-10%)") )] #Gradedbund
gdf7 = gdf[(gdf['LULC'] == 'Arable land') & ((gdf['New_Slope'] == "Gently sloping (3-5%)") )] #Trench cum bund
gdf8 = gdf[(gdf['LULC'] == 'Arable land') & ((gdf['New_Slope'] == "Very gently sloping (1-3%)") )] #Field bunding
gdf9 = gdf[(gdf['New_Slope'] == "Strongly sloping (>25 %)")]    #plantation
gdf10= gdf[(gdf['LULC'] == "River")]
gdf11= gdf[(gdf['LULC'] == "Habitation")]
gdf12= gdf[(gdf['LULC'] == "Waterbody")]





# recreating the table
def add_code(df,code,s):
    rows = len(df)
    id=[]
    nm=[]
    for i in range(rows):
        id.append(code)
        nm.append(s)
    df['StructureId'] = id
    df['StructureName'] = nm
    # df.to_file(f"Product\\{s}.shp")
    return df
    


gdf1 = add_code(gdf1,1,"staggerd Trench")
gdf2 = add_code(gdf2,2,"Trench cum bund - NA")
gdf3 = add_code(gdf3,3,"stonebunding1 ")
gdf4 = add_code(gdf4,4,"stonebunding2 ")
gdf5 = add_code(gdf5,5,"Terrace ")
gdf6 = add_code(gdf6,6,"Graded bund ")
gdf7 = add_code(gdf7,7,"Trench cum bund - A")
gdf8 = add_code(gdf8,8,"Field bunding")
gdf9 = add_code(gdf9,9,"plantation")
gdf10 = add_code(gdf10,10,"River")
gdf11 = add_code(gdf11,11,"Habitation")
gdf12 = add_code(gdf12,12,"Waterbody")
gdff = pd.concat([gdf1,gdf2,gdf3,gdf4,gdf5,gdf6,gdf7,gdf8,gdf9,gdf10,gdf11,gdf12])
# gdff.to_file("Product.shp.zip")


# creating google map object
m = geemap.Map()
m.add_basemap()

style1 =  {"fillColor": "#ff0000", "color": "#ff0000", "weight": 1, "opacity": 0.7} #staggerd Trench
style2 =  {"fillColor": "#00ff00", "color": "#00ff00", "weight": 1, "opacity": 0.7} #Trench cum bund - NA
style3 =  {"fillColor": "#964B00", "color": "#964B00", "weight": 1, "opacity": 0.7} #stonebunding1 
style4 =  {"fillColor": "#FFFF00", "color": "#FFFF00", "weight": 1, "opacity": 0.7} #stonebunding2 
style5 =  {"fillColor": "#0000FF", "color": "#0000FF", "weight": 1, "opacity": 0.7} #Terrace 
style6 =  {"fillColor": "#FFA500", "color": "#FFA500", "weight": 1, "opacity": 0.7} #Graded bund 
style7 =  {"fillColor": "#A020F0", "color": "#A020F0", "weight": 1, "opacity": 0.7} #Trench cum bund - A
style8 =  {"fillColor": "#FFC0CB", "color": "#FFC0CB", "weight": 1, "opacity": 0.7} #Field bunding
style9 =  {"fillColor": "#0B5345", "color": "#0B5345", "weight": 1, "opacity": 0.7} #plantation
style10 = {"fillColor": "#00FFFF", "color": "#00FFFF", "weight": 1, "opacity": 1}   #River
style11 = {"fillColor": "#800000", "color": "#800000", "weight": 1, "opacity": 1}   #Habitation
style12 = {"fillColor": "#EBF5FB", "color": "#EBF5FB", "weight": 1, "opacity": 1}   #Waterbody
style02 = {"color": "#000000", "weight": 10, "opacity": 100}

m.add_gdf(gdf02, layer_name = "Musakani MWS", style = style02)
m.add_gdf(gdf1, layer_name="strycture 1", style = style1)
m.add_gdf(gdf2, layer_name="strycture 2", style = style2)
m.add_gdf(gdf3, layer_name="strycture 3", style = style3)
m.add_gdf(gdf4, layer_name="strycture 4", style = style4)
m.add_gdf(gdf5, layer_name="strycture 5", style = style5)
m.add_gdf(gdf6, layer_name="strycture 6", style = style6)
m.add_gdf(gdf7, layer_name="strycture 7", style = style7)
m.add_gdf(gdf8, layer_name="strycture 8", style = style8)
m.add_gdf(gdf9, layer_name="strycture 9", style = style9)
m.add_gdf(gdf10, layer_name="strycture 10", style = style10)
m.add_gdf(gdf11, layer_name="strycture 11", style = style11)
m.add_gdf(gdf12, layer_name="strycture 12", style = style12)

#Add legend
title = "Mapping the structures"
#dict = {}
dictionary = {
"staggerd Trench":"#ff0000",
"Trench cum bund - NA":"#00ff00",
"stonebunding1 ":"#964B00",
"stonebunding2 ":"#FFFF00",
"Terrace ":"#0000FF",
"Graded bund ":"#FFA500",
"Trench cum bund - A":"#A020F0",
"Field bunding ":"#FFC0CB",
"plantation ":"#0B5345",
"River":"#00FFFF",
"Habitation":"#800000",
"Waterbody":"#EBF5FB"}
  # Define legend entries and their corresponding colors
m.add_legend(title, dictionary)

#display the map
m
