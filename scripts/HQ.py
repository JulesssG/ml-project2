from obspy import read
from obspy import UTCDateTime

start_time_hq = UTCDateTime("2018-04-09T10:22:22.000")
end_time_hq = start_time_hq + 2 * 60

st_hq = read("../processed-data/example-1-day.slist", format="SLIST", starttime=start_time_hq, endtime=end_time_hq)

print(type(st_hq.differentiate()))
print(st_hq.differentiate())
diff = st_hq.differentiate()

diff.plot()

#st = st_hq + diff

#st.plot()

