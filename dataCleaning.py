import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

del df ["Luminosity"]
del df ["Star_name"]

print(list(df))

df.to_csv('total_stars.csv') 