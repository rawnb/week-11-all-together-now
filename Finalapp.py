"""MUSA 509 Final Project"""
import json
import logging

from flask import Flask, request, render_template
from sqlalchemy import create_engine
from sqlalchemy.sql import text
import geopandas as gpd

# load credentials from a file
with open("pg-credentials.json", "r") as f_in:
    pg_creds = json.load(f_in)

# mapbox
with open("mapbox_token.json", "r") as mb_token:
    MAPBOX_TOKEN = json.load(mb_token)["token"]

app = Flask(__name__, template_folder="templates")

# load credentials from JSON file
HOST = pg_creds["HOST"]
USERNAME = pg_creds["USERNAME"]
PASSWORD = pg_creds["PASSWORD"]
DATABASE = pg_creds["DATABASE"]
PORT = pg_creds["PORT"]


def get_sql_engine():
    return create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")


def get_zipcodes():
    """Gets all zipcodes"""
    engine = get_sql_engine()
    query = text(
        """
        SELECT DISTINCT ZIP_CODE as zipcode
        FROM facilityconditionindexsd
        ORDER BY 1 ASC
    """
    )
    resp = engine.execute(query).fetchall()
    # get a list of names
    zipcodes = [row["zipcode"] for row in resp]
    return zipcodes


# index page
@app.route("/")
def index():
    """Index page"""
    codes = get_zipcodes()
    return render_template("input.html", ccode=codes)


# New damage calculation function

def get_centroid(ccode):
    """Gets earthquake epicenter centroid"""
    query = text(
    """
    SELECT DISTINCT GEOM as geom
    FROM facilityconditionindexsd as f
    WHERE f.ZIP_CODE = :ccode
    """
    )
    resp = engine.execute(query, ccode=ccode).fetchone()
    return resp["geom"]

def get_damage():
    """Calculated damage for each point"""
    engine = get_sql_engine()
    centroid = get_centroid()
    query = text(
        """
        WITH part1 as 
    (SELECT p.building_name, p.location_description, p.capital_req, p.BLDG_DESC, 
    ST_Distance(geom::geography, ST_SetSRID(ST_MakePoint(lng_zip, lat_zip), 4326)::geography) as distance, 
    multiplier*shakeability*p.capital_req as damage
    FROM(
      SELECT capital_req, 
      SUM(CASE WHEN distance < .5 THEN 1 ELSE 0 END) as multiplier, 
      SUM(CASE WHEN distance < 1 THEN .5 ELSE 0 END) as multiplier, 
      SUM(CASE WHEN distance >= 1 THEN .25 ELSE 0 END) as multiplier, 
    FROM pgadmin as p

    SELECT 
    building_name, 
    location_description,
    capital_req, 
    BLDG_DESC,
    distance,
    damage
    FROM part1
    ORDER BY damage
             
    """
        )







#Old building viewer functions

def get_bounds(geodataframe):
    """returns list of sw, ne bounding box pairs"""
    bounds = geodataframe.geom.total_bounds
    bounds = [[bounds[0], bounds[1]], [bounds[2], bounds[3]]]
    return bounds


def get_num_buildings(ccode):
    """Get number of buildings in a zipcode"""
    engine = get_sql_engine()
    building_stats = text(
        """
        SELECT
          COUNT(building_name) as num_buildings, community_area
        FROM facilityconditionindexsd as f
        WHERE f.ZIP_CODE = :ccode
        GROUP BY 2 
    """
    )
    resp = engine.execute(building_stats, ccode=ccode).fetchone()
    return resp["num_buildings"]


def get_zipcode_buildings(ccode):
    """Get all buildings for a zipcode"""
    engine = get_sql_engine()
    vacant_buildings = text(
        """
        SELECT
            location_description, total_req, desc_full, geom
        FROM facilityconditionindexsd as f
        WHERE f.ZIP_CODE = :ccode
    """
    )
    buildings = gpd.read_postgis(vacant_buildings, con=engine, params={"ccode": ccode})
    return buildings


@app.route("/buildingviewer", methods=["GET"])
def building_viewer():
    """Test for form"""
    code = request.args["zipcode"]
    buildings = get_zipcode_buildings(code)
    bounds = get_bounds(buildings)

    # generate interactive map
    map_html = render_template(
        "geojson_map.html",
        geojson_str=buildings.to_json(),
        bounds=bounds,
        center_lng=(bounds[0][0] + bounds[1][0]) / 2,
        center_lat=(bounds[0][1] + bounds[1][1]) / 2,
        mapbox_token=MAPBOX_TOKEN,
    )
    return render_template(
        "vacant.html",
        num_buildings=get_num_buildings(code),
        ccode=code,
        map_html=map_html,
        buildings=buildings[["location_description", "total_req", "desc_full"]].values,
    )


# 404 page example
@app.errorhandler(404)
def page_not_found(err):
    """404 page"""
    return f"404 ({err})"


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True)

