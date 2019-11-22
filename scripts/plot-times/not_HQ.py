from obspy import read
from obspy import UTCDateTime

start_time = UTCDateTime("2018-04-09T13:34:50.000")
end_time = start_time + 9 * 60

st = read("../../processed-data/example-1-day.slist", format="SLIST", starttime=start_time, endtime=end_time)

st.differentiate().plot()

