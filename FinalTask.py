import math
import sqlite3


def calculate_distance(lat1, lon1, lat2, lon2):
    return 6371 * math.acos(math.sin(math.radians(lat1)) * math.sin(math.radians(lat2)) +
                           math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
                           math.cos(math.radians(lon2) - math.radians(lon1)))

def find_coordinates(city_name):
    conn = sqlite3.connect('coordinates.db')
    cursor = conn.cursor()
    cursor.execute("SELECT latitude, longitude FROM coordinates WHERE city_name=?", (city_name,))
    result = cursor.fetchone()
    if result is not None:
        latitude, longitude = result
        lat=latitude
        log=longitude
    else:
        lat=input(f"Please, enter the latitude for {city_name}")
        log=input(f"Please, enter the longitude for {city_name}")
        cursor.execute("INSERT INTO coordinates (city_name, latitude, longitude) VALUES (?, ?, ?)",(city_name, lat, log))
        conn.commit()
    cursor.close()
    conn.close()
    return lat,log

def find_distance():
    city1 = input("Please write the name of the first city ")
    city2 = input("Please write the name of the second city ")
    lat1, lon1 = find_coordinates(city1)
    lat2, lon2 = find_coordinates(city2)
    result = calculate_distance(float(lat1), float(lon1), float(lat2), float(lon2))
    print(f"Distance between {city1} and {city2} is {result} kilometers")
    return result

find_distance()

