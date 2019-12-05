from multiprocessing import Process
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
client = Client("IRIS")

# Change the first -> +45 days
t1 = UTCDateTime("2018-01-01T00:00:00.000")
t2 = t1 + 2*24*3600
t3 = t2 + 2*24*3600
t4 = t3 + 2*24*3600

# Change number of directory for each function
# ---> Need to mkdir for each function before
# --> for i in {1..12};do mkdir downloads/$i;done in scripts/
def first():
    st = client.get_waveforms("GS", "OK029", "*", "HH1", t1, t2)
    for i, trace in enumerate(st):
        trace.write(f"downloads/1/{i}.slist", format="SLIST")
    print('done 1')

def second():
    st = client.get_waveforms("GS", "OK029", "*", "HH1", t2, t3)
    for i, trace in enumerate(st):
        trace.write(f"downloads/2/{i}.slist", format="SLIST")
    print('done 2')

def third():
    st = client.get_waveforms("GS", "OK029", "*", "HH1", t3, t4)
    for i, trace in enumerate(st):
        trace.write(f"downloads/3/{i}.slist", format="SLIST")
    print('done 3')
processes = [Process(target=first), Process(target=second), Process(target=third)]

for p in processes:
    p.start()

for p in processes:
    p.join()
