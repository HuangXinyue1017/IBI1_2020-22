import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import the file
covid_data = pd.read_csv("full_data.csv")
#print(covid_data)

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
ax.legend()
plt.show()