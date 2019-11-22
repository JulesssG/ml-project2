from obspy import read
from obspy import UTCDateTime

start_time_hq = UTCDateTime("2018-04-09T14:00:00.000")
end_time_hq = start_time_hq + 10 * 60

st_hq = read("../../processed-data/example-1-day.slist", format="SLIST", starttime=start_time_hq, endtime=end_time_hq)

st_hq.plot()

