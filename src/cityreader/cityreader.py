# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

import csv


class City():
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  def __repr__(self):
      return f'City("{self.name}", {self.lat}, {self.lon})'


cities = []

def cityreader(cities=[]):
    with open("cities.csv") as city_file:
        city_reader = csv.DictReader(city_file, delimiter=",")
        for row in city_reader:
            city = City(row["city"], float(row["lat"]), float(row["lng"]))
            cities.append(city)
    
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

#def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
#    lats = [lat1, lat2]
#    lats.sort()
#    lons = [lon1, lon2]
#    lons.sort()
    # within will hold the cities that fall within the specified region
#    within = [city for city in cities
#              if float(city.lat) >= lats[0]
#              and float(city.lat) <= lats[1]
#              and float(city.lon) >= lons[0]
#              and float(city.lon) <= lons[1]]
    # TODO Ensure that the lat and lon values are all floats
    # Go through each city and check to see if it falls within
    # the specified coordinates.
#    return within
