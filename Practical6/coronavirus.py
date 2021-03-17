import matplotlib.pyplot as plt

# A dictionary about coronavirus infection rate
dictionary = {'USA':29862124, 'India':11285561, 'Brazil':11205972, 'Russia':4360823, 'UK':4234924}

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK'
sizes = [29862124, 11285561, 11205972, 4360823, 4234924]
explode = (0, 0, 0.1, 0, 0)  # only "explode" the 1nd slice (i.e. 'Brazil')

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()