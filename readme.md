Greenprints Bioregion Data Merge Tool
==========

## Installation

Install all tools required on Ubuntu:

    sudo apt install python3 python3-pip git build-essential libsqlite3-dev zlib1g-dev
    pip3 install geopandas
    mkdir data
    git clone https://github.com/mapbox/tippecanoe.git
    cd tippecanoe
    make -j
    make install

## Usage

Download the bioregion and sub-bioregion shapefile data from the [IBRA website](https://www.environment.gov.au/land/nrs/science/ibra) and save them into the data/ folder.

Run the following command to convert the shapefile data into GeoJSON:

    python3 convert_shp.py

Edit the template data in region_data.xlsx and subregion_data.xlsx to provide all data to be merged into the bioregion datasets.

Run the following command to merge the data:

    python3 merge_regiondata.py

Merge the Greenprints data with the GeoJSON

    TO BE COMPLETED

Convert the GeoJSON to mapbox vertor tile format used by the mapping server:

    bash create_mbtiles.sh

Upload the .mbtiles files to the server and restart the [mbtileserver](https://github.com/consbio/mbtileserver) instance.
