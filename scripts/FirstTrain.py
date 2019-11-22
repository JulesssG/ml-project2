from obspy.clients.fdsn import Client

from obspy import UTCDateTime

client = Client("IRIS")
from obspy.clients.fdsn.header import URL_MAPPINGS

for key in sorted(URL_MAPPINGS.keys()):
    print("{0:<7} {1}".format(key,  URL_MAPPINGS[key]))


starttime = UTCDateTime("2016-07-01")
endtime = UTCDateTime("2016-07-12")

inventory = client.get_stations(network="OK", station="*",
                                starttime=starttime,
                                endtime=endtime)
print(inventory)

inventory = client.get_stations(network="GS", station="OK*",
                                starttime=starttime,
                                endtime=endtime)
print(inventory)


t = UTCDateTime("2018-04-09T00:00:00.000")

st = client.get_waveforms("GS", "OK029", "*", "HH1", t, t + 4 * 24 * 60 * 60)
st.write("first-train.slist", format="SLIST")
st.plot()
