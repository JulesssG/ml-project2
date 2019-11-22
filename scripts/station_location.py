from obspy.clients.fdsn import Client
from obspy import UTCDateTime

def get_location(network, station, channel):
    client = Client("IRIS")

    inventory = client.get_stations(network="GS", station="OK029", channel="HH1")

    station = inventory[0][0]

    latitude = station.latitude
    longitude = station.longitude

    return latitude, longitude

def compute_distance(source_lat, source_lon, to_lat, to_lon):
    raise NotImplementedError

