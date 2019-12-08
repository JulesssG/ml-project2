from multiprocessing import Process
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import datetime
client = Client("IRIS")

t1 = UTCDateTime(datetime.datetime(2018, 1, 30, 17,45))
t2 = t1 + 20*60


st = client.get_waveforms("GS", "OK029", "*", "HH1", t1, t2)
st.plot()
