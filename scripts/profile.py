import pandas as pd
import os
from ydata_profiling import ProfileReport
car_dataset = pd.read_csv('data/cardata.csv')
profile = ProfileReport(car_dataset, title= "Car Data Profiling Report")
profile.to_file('profiling/report.html')