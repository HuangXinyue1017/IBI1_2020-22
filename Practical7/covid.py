import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import the file
covid_data = pd.read_csv("full_data.csv")
#print(covid_data)

# all columns and every second row
print(covid_data.iloc[0:10:2,0:6])

# use boolean to show "total_cases"
Af = covid_data[covid_data["location"] == "Afghanistan"]
want = [False, False, False, False, True, False]
print(Af.iloc[:,want])

# compute mean and median of new cases for the entire world
world = covid_data[covid_data["location"] == "World"]
check = [True, False, True, False, False, False]
print(world.iloc[:,check].describe())

# create a boxplot of new cases worldwide
check = [False, False, True, False, False, False]
bp_data = world.iloc[:,check]

# plot both new cases and new deaths worldwide
plt.boxplot(bp_data)
plt.show()

# plot dates as x and new_cases as y
check = [True, False, False, False, False, False]
world_dates = world.iloc[:,check]
x = np.array(world_dates.values.T)
x = x[0]

check = [False, False, True, False, False, False]
world_new_cases = world.iloc[:,check]
y = np.array(world_new_cases.values.T)
y = y[0]

# z label name
# pos label position
z = world_dates.iloc[0:len(world_dates):4]
z = np.array(z.values.T)
z = z[0]

pos = list(range(len(world_dates)))[::4]

plt.xticks(pos, z.tolist(), rotation = -90)
plt.ylabel('number')
plt.title('Total cases')
plt.plot(x, y, 'b+')
plt.show()

# answer the question in question.txt
# new cases and total cases developed over time in Spain
spain = covid_data[covid_data["location"] == "Spain"]

check = [True, False, False, False, False, False]
spain_dates = spain.iloc[:,check]
d = np.array(spain_dates.values.T)
d = d[0]

check = [False, False, True, False, False, False]
spain_new_cases = spain.iloc[:,check]
a = np.array(spain_new_cases.values.T)
a = a[0]

check = [False, False, False, False, True, False]
spain_total_cases = spain.iloc[:,check]
b = np.array(spain_total_cases.values.T)
b = b[0]

z = spain_dates.iloc[0:len(spain_dates):4]
z = np.array(z.values.T)
z = z[0]

pos = list(range(len(spain_dates)))[::4]

plt.xticks(pos, z.tolist(), rotation = -90)
plt.ylabel('number')
plt.title('New Cases and Total Cases in Spain')
plt.plot(d, a, 'b+')
plt.plot(d, b, 'r-')
plt.show()