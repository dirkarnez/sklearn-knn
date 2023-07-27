data = [[5, 1], [4, 0], [1, 3], [0, 4]]
movie_type = ["action", "action", "sci-fi", "sci-fi"]

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(data, movie_type)
print(neigh.predict([[3, 0]])) # "action"