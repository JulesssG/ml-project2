from multiprocessing import Process
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import datetime
client = Client("IRIS")

# Change num_delay, if downloading 7,8,9 -> 2
base = UTCDateTime("2018-01-01T00:00:00.000")
num_delay = 3
t1 = UTCDateTime(base.datetime + num_delay * datetime.timedelta(days=45))
t2 = t1 + 15*24*3600
t3 = t2 + 15*24*3600
t4 = t3 + 15*24*3600

# Change number of directory for each function
# run script from root (python scripts/down...) or change the path
# ---> Need to mkdir for each function before
# --> for i in {X,X+1,X+2};do mkdir data/downloads/$i;done in scripts/
def first():
    st = client.get_waveforms("GS", "OK029", "*", "HH1", t1, t2)
    try:
        for i, trace in enumerate(st):
            trace.write(f"data/downloads/10/{i}.slist", format="SLIST")
    except FileNotFoundError:
        print("Wrong setup, file not found error")

    print('done 1')

def second():
    st = client.get_waveforms("GS", "OK029", "*", "HH1", t2, t3)
    try:
        for i, trace in enumerate(st):
            trace.write(f"data/downloads/11/{i}.slist", format="SLIST")
    except FileNotFoundError:
        print("Wrong setup, file not found error")

    print('done 2')

def third():
    st = client.get_waveforms("GS", "OK029", "*", "HH1", t3, t4)
    try:
        for i, trace in enumerate(st):
            trace.write(f"data/downloads/12/{i}.slist", format="SLIST")
    except FileNotFoundError:
        print("Wrong setup, file not found error")

    print('done 3')

processes = [Process(target=first), Process(target=second), Process(target=third)]
for p in processes:
    p.start()

for p in processes:
    p.join()
