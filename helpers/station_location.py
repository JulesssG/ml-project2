from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import math
from math import cos, sin, sqrt, radians


def get_location(network, station, channel):
    """
    Used to get the geographic location of a station
    """
    client = Client("IRIS")

    inventory = client.get_stations(network="GS", station="OK029", channel="HH1")

    station = inventory[0][0]

    latitude = station.latitude
    longitude = station.longitude
    elevation = station.elevation

    return latitude, longitude, elevation


def geographic_to_ECEF(lat, lon, h):
    """
    Used to compute the distance between an earthquake
    and the location of a station
    """
    a = 6378137  # Earth radius equator
    e_2 = 0.00669437999 # Eccentricity of ellipsoid (WGS-84)
    b = a * sqrt(1-e_2)

    R = a/sqrt(1 - e_2 * sin(lat)**2)

    x = (R + h) * cos(lat) * cos(lon)
    y = (R + h) * cos(lat) * sin(lon)
    z = (R + h - e_2 * R) * sin(lat)

    return x, y, z


def compute_distance(lat1, lon1, h1, lat2, lon2, h2):
    """
    Compute the euclidian distance between two geographic locations
    """
    x1, y1, z1 = geographic_to_ECEF(radians(lat1), radians(lon1), h1)
    x2, y2, z2 = geographic_to_ECEF(radians(lat2), radians(lon2), h2)

    dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
    return dist
