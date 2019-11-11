from obspy import read

st = read("../processed-data/example-1-day.slist", format="SLIST")
st.plot()
