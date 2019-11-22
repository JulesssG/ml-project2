from obspy import read
from obspy import UTCDateTime

st_1_day = read("../../processed-data/example-1-day.slist", format="SLIST")

st_1_day.plot()

