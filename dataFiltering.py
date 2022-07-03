import pandas as pd
import  matplotlib.pyplot as plt
import csv

df = pd.read_csv("starsChart.csv")

rows = []

with open("starsChart.csv",'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

star_data_rows=rows[1:]

star_masses = []
star_distance = []
star_names = []
star_gravity=[]

for star_data in star_data_rows:
  star_masses.append(star_data[3])
  star_distance.append(star_data[2])
  star_names.append(star_data[1])
  star_gravity.append(star_data[5])

dist_stars = []
for star_data in star_data_rows:
  if float(star_data[2]) <= 100:
    dist_stars.append(star_data)

gravity_stars = []
for star_data in dist_stars:
  if float(star_data[5]) > 150 and float(star_data[5]) < 350:
    gravity_stars.append(star_data)

data = gravity_stars
df = pd.DataFrame(data, columns=['', 'Name', 'Distance', 'Mass', 'Radius', 'Gravity'])
df.to_csv("filteredStarsChart.csv", index=False)