import numpy as np
import geocoder
import sqlite3
from ipstack import GeoLookup
from requests import get
import googlemaps

    

connection = sqlite3.connect("HorizonHacks.db", check_same_thread=False)
cursor = connection.cursor()
"""ip = get('https://api.ipify.org').text

    geo_lookup = GeoLookup("63096ef2c875f22104912c0dafdb2af0")
    try:
        location = geo_lookup.get_location(str(ip))
        if location is None:
            print("Failed to find location.")
        else:
            # Print the Location dictionary.
            u_latitude=(location['latitude'])
            u_longitude=(location['longitude'])
    except Exception as e:
        print(e)"""


def setup_database():

    command1 = """CREATE TABLE IF NOT EXISTS
    profiles(full_name TEXT, email_address TEXT, password TEXT, flag INTEGER)"""

    command2 = """CREATE TABLE IF NOT EXISTS
    stores(owner_name TEXT, name TEXT, location TEXT, menu TEXT, description TEXT, lat REAl, lon REAL)"""

    cursor.execute(command1)
    cursor.execute(command2)


def register( name, email, password, owner_name, b_name, location, menu, description):
    cursor.execute(
        "INSERT INTO profiles VALUES ('{}', '{}', '{}', 0)".format(
            name, email, password
        )
    )

    gmaps = googlemaps.Client(key='AIzaSyB9sx96qabluloodazrX5o-PSKcSn1zhNs')

    geocode_result = gmaps.geocode(location)
    x = geocode_result[0]['geometry']['location']
    print(x)
    cursor.execute(
        "INSERT INTO stores VALUES ('{}', '{}', '{}', '{}', '{}', {}, {})".format(
            owner_name, b_name, location, menu, description, x['lat'], x['lng']
        )
    )
    print_stores()
    print_login()


def print_login():
    cursor.execute("SELECT * FROM profiles")
    print(cursor.fetchall())

def validate(email, password):
    print_login()
    cursor.execute("SELECT * FROM profiles")
    data = cursor.fetchall()
    connection.commit()

    print(data)
    for i in data:
        print(type(i[1]))
        print(i[2])
        if i[1] == email and i[2] == password:
            return True
    return False



def get_store_data():
    cursor.execute("SELECT * FROM stores")
    connection.commit()
    return (cursor.fetchall())

def print_stores():
    cursor.execute("SELECT * FROM stores")
    print(cursor.fetchall())



def print_distance_between( location_user=[]):
    cursor.execute("SELECT * FROM stores")
    data = cursor.fetchall()
    print(data)
    distances = []
    for i in data:
        r = 6371
        lat1, lon1 = location_user[0], location_user[1]
        lat2, lon2 = float(i[4]), float(i[5])
        phi1 = np.radians(lat1)
        phi2 = np.radians(lat2)
        delta_phi = np.radians(lat2 - lat1)
        delta_lambda = np.radians(lon2 - lon1)
        a = (
            np.sin(delta_phi / 2) ** 2
            + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
        )
        res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
        distances.append(np.round(res, 2))

    return [x for _, x in sorted(zip(distances, data))]
