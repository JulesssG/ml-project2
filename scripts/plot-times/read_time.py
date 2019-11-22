from obspy.clients.fdsn import Client

from obspy import UTCDateTime

client = Client("IRIS")
from obspy.clients.fdsn.header import URL_MAPPINGS


startTime = UTCDateTime("2018-04-11T00:21:00.000")
endTime = startTime + 2 * 60

st = client.get_waveforms("GS", "OK029", "*", "HH1", startTime, endTime)
st.write("example-1-day.slist", format="SLIST")
st.plot()
