import numpy as np
import geocoder
import sqlite3
from ipstack import GeoLookup
from requests import get

'''ip = get('https://api.ipify.org').text

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
        print(e)'''



def setup_database():
    connection = sqlite3.connect('HorizonHacks.db')
    cursor = connection.cursor()

    command1 = """CREATE TABLE IF NOT EXISTS
    profiles(full_name TEXT, email_address TEXT, password TEXT, flag INTEGER)"""

    command2 = """CREATE TABLE IF NOT EXISTS
    stores(owner_name TEXT, name TEXT, location TEXT, menu TEXT, description TEXT, lat REAl, lon REAL)"""
    connection.close()

    cursor.execute(command1)
    cursor.execute(command2)

def register(name, email, password, b_name, location, menu, description):
    connection = sqlite3.connect('HorizonHacks.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO profiles VALUES ('{}', '{}', '{}', 0)".format(name, email, password))

    g = geocoder.arcgis(location)
    temp = g.json
    coordinates = [temp['lat'], temp['lng']]
    cursor.execute("INSERT INTO stores VALUES ('{}', '{}', '{}', '{}', {}, {})".format(b_name, location, menu, description, coordinates[0], coordinates[1]))
    connection.close()


def print_login(cursor):
    connection = sqlite3.connect('HorizonHacks.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM profiles')
    print(cursor.fetchall())
    connection.close()


def print_stores(cursor):
    connection = sqlite3.connect('HorizonHacks.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM stores')
    print(cursor.fetchall())
    connection.close()



def print_distance_between(cursor, location_user = []):
    connection = sqlite3.connect('HorizonHacks.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM stores')
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
        a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) *   np.sin(delta_lambda / 2)**2
        res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
        distances.append(np.round(res, 2))
    connection.close()

    return [x for _,x in sorted(zip(distances,data))]

