### ATTEMPTED ELEVATION STUFF ###

import googlemaps
from googlemaps import convert

googmaps = googlemaps.Client(key = "AIzaSyDX55su6U0BGQnZSLfxNkmrSMUM6fGldYw")

def location_geocode(user_location):
    return googmaps.geocode(user_location)

def latlong(location_geocode):
    latlong_dict=location_geocode[0]['geometry']['location']
    latlong_location=latlong_dict['lat'], latlong_dict['lng']
    return latlong_location

def path_elevation(user_location, destination, samples):
    start_location = location_geocode(user_location)
    end_location = location_geocode(destination)
    path = [latlong(start_location), latlong(end_location)]
    return googmaps.elevation_along_path(path, samples)

### CALCULATING TIME ###

""" Variables to account for:
    1) real_dist: which we will get from distance travelled and the elevation of the distance from elevation function)
    2) get_speed: which is the speed at which a person walks given FITBIT data
    3) classes: which is the number of classes during the time frame in which the person is travelling."""

def real_time(real_dist, get_speed, day, time):
    assert 0 <= time <= 24
    if day == Saturday or day == Sunday:
        return real_dist * get_speed
    else:
        if 14 <= time <= 16 or 10 <= time <= 12:
            affected_speed = get_speed * 0.8
            return real_dist * affected_speed
        elif 8 <= time <= 10 or 12 <= time <= 14:
            affected_speed = get_speed * 0.9
            return real_dist * affected_speed
        else:
            return real_dist * get_speed
