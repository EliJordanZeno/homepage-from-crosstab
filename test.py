import pandas as pd
import numpy as np

import chardet

file_name = "Regeneron_Corp_Dig_LinkedIn_Analytics_Report.csv"

with open(file_name, 'rb') as rawdata:
    result = chardet.detect(rawdata.read(100000))
    print(result)

df = pd.read_csv(file_name,encoding="utf-16",encoding_errors="ignore",on_bad_lines='skip')

print(df)
