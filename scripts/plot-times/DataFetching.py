#
# This file is part of OK.
#
# Created by Brice Lecampion on 06.11.19.
# Copyright (c) ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, Geo-Energy Laboratory, 2016-2019.  All rights reserved.
# See the LICENSE.TXT file for more details. 
#



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


# get data for a time
#t = UTCDateTime("2016-07-01T06:45:00.000")
#
#st = client.get_waveforms("OK", "NOKA", "*", "HHN,HHE,HHZ", t, t + 60 * 60)
#
#st.plot()
#
#st = client.get_waveforms("GS", "OK038", "*", "HHN,HHE,HHZ", t, t + 60 * 60)
#
#st = client.get_waveforms("GS", "OK029", "*", "HHN", t, t + 60 * 60)

t = UTCDateTime("2018-04-11T23:37:08.000")
st = client.get_waveforms("GS", "OK029", "*", "HH1", t, t + 2)
#st.write("example-1-day.slist", format="SLIST")
st.plot()
