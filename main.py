import csv
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
from matplotlib import pyplot as plt

#for storing x coordinates
arr1 = []
#for storing y coordinates (will later be combined with arr1 into a 2d arr)
arr2 = []


#open csv file and load the x & y coordinates
with open('clusterplot.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        #print(row)
        #print(row[0])
        #print(row[0], row[1], row[2], )
        arr1.append(row[1])
        arr2.append(row[2])

#get rid of the first line from csv
arr1.pop(0)
arr2.pop(0)

#print(arr1)
#print(arr2)

#create np arr out of the lists
x1 = np.array(arr1)
x2 = np.array(arr2)

plt.plot()
#combine the np arrays into 2d arr
X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)


colors = ['b', 'g', 'r']
markers = ['o', 'v', 's']


distortions = []
for k in range(2, 20):
    kmeans = KMeans(n_clusters=k).fit(X)
    kmeans.fit(X)
    distortions.append(sum(np.min(cdist(X, kmeans.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])

plt.plot(range(2, 20), distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()

#from this plot, determine optimal k