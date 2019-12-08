from multiprocessing import Process
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import datetime
client = Client("IRIS")

# Take 1 month
base = UTCDateTime("2019-01-01T00:00:00.000")
t1 = UTCDateTime(base.datetime)
t2 = t1 + 10*24*3600
t3 = t2 + 10*24*3600
t4 = t3 + 10*24*3600

def first():
    st = client.get_waveforms("GS", "OK029", "*", "HH1", t1, t2)
    try:
        for i, trace in enumerate(st):
            trace.write(f"data/downloads/test/1/{i}.slist", format="SLIST")
    except FileNotFoundError:
        print("Wrong setup, file not found error")

    print('done 1')

def second():
    st = client.get_waveforms("GS", "OK029", "*", "HH1", t2, t3)
    try:
        for i, trace in enumerate(st):
            trace.write(f"data/downloads/test/2/{i}.slist", format="SLIST")
    except FileNotFoundError:
        print("Wrong setup, file not found error")

    print('done 2')

def third():
    st = client.get_waveforms("GS", "OK029", "*", "HH1", t3, t4)
    try:
        for i, trace in enumerate(st):
            trace.write(f"data/downloads/test/3/{i}.slist", format="SLIST")
    except FileNotFoundError:
        print("Wrong setup, file not found error")

    print('done 3')

processes = [Process(target=first), Process(target=second), Process(target=third)]
for p in processes:
    p.start()

for p in processes:
    p.join()
