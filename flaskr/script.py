import Database_test
import sqlite3
from ipstack import GeoLookup
from requests import get

ip = get('https://api.ipify.org').text

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
    print(e)

connection = sqlite3.connect('HorizonHacks.db')
cursor = connection.cursor()
Database_test.setup_database(cursor)
print("Hello, Welcome to my Test Trial!")
choice = input("Are you a business owner, or a customer? (b, or c): ")
if choice == 'b':
    b_name = input("What is the name of the business?: ")
    b_location = input("What is the location of the business?: ")
    b_menu = input("What is the menu of your business?: ")
    b_description = input("Describe your business: ")
    Database_test.add_to_stores(cursor, b_name, b_location, b_menu, b_description)
elif choice == 'c':
    c_name = input('What is your name?: ')
    c_email = input('What is your email address?: ')
    Database_test.add_to_login_database(cursor, c_name, c_email)

print()
for i in Database_test.print_distance_between(cursor, [u_latitude, u_longitude]):
    print(i[0])