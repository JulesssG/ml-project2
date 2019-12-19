"""
Script used to easily visualize a channel during a period of time.
"""
from multiprocessing import Process
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import datetime
client = Client("IRIS")

t1 = UTCDateTime(datetime.datetime(2018, 1, 1, 0, 0))
t2 = t1 + 60


st = client.get_waveforms("GS", "OK029", "*", "HH1", t1, t2)
st.plot()
