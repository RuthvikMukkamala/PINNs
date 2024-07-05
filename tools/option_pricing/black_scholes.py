from typing import List
from gs_quant.data import Dataset
from datetime import date



weather_ds = Dataset('WEATHER')
data_frame = weather_ds.get_data(date(2016, 1, 1),  date(2016, 1, 31), city=["Boston"])

print(data_frame)