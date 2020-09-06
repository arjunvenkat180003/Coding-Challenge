# ACM Research Coding Challenge (Fall 2020)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using . `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Email the link of your repo to research@acmutd.co with the same email you used to submit your application. Be sure to include your name in the email.

## Question One

![Image of Cluster Plot](ClusterPlot.png)
<br/>
Given the following dataset in `ClusterPlot.csv`, determine the number of clusters by using any clustering algorithm. **You're allowed to use any Python library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file.


My solution:

My solution was to use a the "Elbow method", to plot the the number of clusters vs distortion, to determine the optimal number of clusters (k), which is used by the k-means algorithm. You iterate from 1 to a large number of clusters, and apply k-means to the data set for each number as k. As you plot the graph, after a certain point, the amount of distortion per new cluster decreases drastically (diminishing returns), and that point (the "elbow" of the curve) gives you a good idea of the number of clusters in the data set. Looking at the curve, the elbow is approximately at 3 on the x-axis, so there are approximately 3 clusters in the data set.

The main libraries I used are the sklearn (sci-kit learn) library, scipy, and numpy (for doing most of the calculation work). matplotlib was used for the graph. I also used the csv library for reading the csv file. 

Code was adapted from https://pythonprogramminglanguage.com/kmeans-elbow-method/ to work with the data set.

Kmeans elbow method. (n.d.). Retrieved from https://pythonprogramminglanguage.com/kmeans-elbow-method/

Additional research was done with the following sources:

Elbow method (clustering). (2020, April 21). Retrieved from https://en.wikipedia.org/wiki/Elbow_method_(clustering)

Franklin, S. J. (2019, November 26). Elbow method of K-means clustering algorithm. Retrieved from https://medium.com/analytics-vidhya/elbow-method-of-k-means-clustering-algorithm-a0c916adc540

