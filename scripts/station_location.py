from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import math
from math import cos, sin, sqrt, radians


def get_location(network, station, channel):
    client = Client("IRIS")

    inventory = client.get_stations(network="GS", station="OK029", channel="HH1")

    station = inventory[0][0]

    latitude = station.latitude
    longitude = station.longitude
    elevation = station.elevation

    return latitude, longitude, elevation


a = 6378137  # Earth radius equator
b = 6356752.314245  # Earth radius poles


def N(lat):
    return a ** 2 / sqrt(a ** 2 * cos(lat) ** 2 + b ** 2 * sin(lat) ** 2)


def geographic_to_ECEF(lat, lon, h):
    x = (N(lat) + h) * cos(lat) * cos(lon)
    y = (N(lat) + h) * cos(lat) * sin(lon)
    z = (b ** 2 / a ** 2 * N(lat) + h) * sin(lat)

    return x, y, z


def compute_distance(lat1, lon1, h1, lat2, lon2, h2):
    x1, y1, z1 = geographic_to_ECEF(radians(lat1), radians(lon1), h1)
    x2, y2, z2 = geographic_to_ECEF(radians(lat2), radians(lon2), h2)

    dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
    return dist
