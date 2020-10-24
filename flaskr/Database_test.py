import numpy as np
import geocoder
def setup_database(cursor):
    command1 = """CREATE TABLE IF NOT EXISTS
    profiles(name TEXT, email_address TEXt)"""

    command2 = """CREATE TABLE IF NOT EXISTS
    stores(name TEXT, location TEXt, menu TEXT, description TEXT, lat REAl, lon REAL)"""

    cursor.execute(command1)
    cursor.execute(command2)
def add_to_login_database(cursor, name, email):
    cursor.execute("INSERT INTO profiles VALUES ('{}', '{}')".format(name, email))

def add_to_stores(cursor, name, location, menu, description):
    g = geocoder.arcgis(location)
    temp = g.json
    coordinates = [temp['lat'], temp['lng']]
    cursor.execute("INSERT INTO stores VALUES ('{}', '{}', '{}', '{}', {}, {})".format(name, location, menu, description, coordinates[0], coordinates[1]))


def print_login(cursor):
    cursor.execute('SELECT * FROM profiles')
    print(cursor.fetchall())


def print_stores(cursor):
    cursor.execute('SELECT * FROM stores')
    print(cursor.fetchall())


def print_distance_between(cursor, location_user = []):
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
    return [x for _,x in sorted(zip(distances,data))]