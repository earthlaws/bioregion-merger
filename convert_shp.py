from glob import glob
import geopandas as gpd

for filename in glob('data/*.shp'):
    file = gpd.read_file(filename)
    file.to_file(filename[:-4] + ".json", driver="GeoJSON")
