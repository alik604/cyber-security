import numpy as np
import pandas as pd

# Remove duplicates
data_all = pd.read_csv('list of password with duplicates.csv')
# data_all = np.genfromtxt('list of password with duplicates.csv', delimiter=',')

print(data_all.shape)

data_unique = np.unique(data_all)
print(data_unique.shape)

data_unique = np.sort(data_unique)
data_unique = data_unique.reshape(1,-1)[0]


f = open('data without duplicates.csv','w')
for line in data_unique:
    l = line
    f.write(line +'\n') 
f.close()
print("Done. Printing results")

print(data_unique)
