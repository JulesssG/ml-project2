from multiprocessing import Process
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
from obspy.clients.fdsn.header import URL_MAPPINGS
client = Client("IRIS")

#for key in sorted(URL_MAPPINGS.keys()):
#    print("{0:<7} {1}".format(key,  URL_MAPPINGS[key]))
#
#
#starttime = UTCDateTime("2017-01-01")
#endtime = UTCDateTime("2018-12-31")
#
#inventory = client.get_stations(network="OK", station="*",
#                                starttime=starttime,
#                                endtime=endtime)
#print(inventory)
#
#inventory = client.get_stations(network="GS", station="OK*",
#                                starttime=starttime,
#                                endtime=endtime)
#print(inventory)


t2017_1 = UTCDateTime("2018-01-01T00:00:00.000")

def first():
    st = client.get_waveforms("GS", "OK029", "*", "HH1", t2017_1, t2017_1 + 60 * 24 * 60 * 60)
    st.write("jan_to_feb_2018_C1.slist", format="SLIST")
    print('done 1')

def second():
    st = client.get_waveforms("GS", "OK029", "*", "HH2", t2017_1, t2017_1 + 60 * 24 * 60 * 60)
    st.write("jan_to_feb_2018_C2.slist", format="SLIST")
    print('done 2')

def third():
    st = client.get_waveforms("GS", "OK029", "*", "HHZ", t2017_1, t2017_1 + 60 * 24 * 60 * 60)
    st.write("jan_to_feb_2018_CZ.slist", format="SLIST")
    print('done 3')

p1 = Process(target=first)
p2 = Process(target=second)
p3 = Process(target=third)
p1.start()
p2.start()
p3.start()
p1.join()
p2.join()
p3.join()

#st = client.get_waveforms("GS", "OK029", "*", "HH1", t2018_1, t2018_1 + 7 * 24 * 60 * 60)
#st.write("oneweek_2018_1.slist", format="SLIST")
#print('done')

#st = client.get_waveforms("GS", "OK029", "*", "HH1", t2017_2, t2017_2 + 7 * 24 * 60 * 60)
#st.write("oneweek_2017_2.slist", format="SLIST")
#print('done')

#st = client.get_waveforms("GS", "OK029", "*", "HH1", t2018_2, t2018_2 + 7 * 24 * 60 * 60)
#st.write("oneweek_2018_2.slist", format="SLIST")
