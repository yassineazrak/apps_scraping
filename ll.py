from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from pprint import pprint
documents = ["the young french men crowned world champions",
             "Google Translate app is getting more intelligent everyday",
             "Facebook face recognition is driving me crazy",
             "who is going to win the Golden Ball title this year",
             "these camera apps are funny",
             "Croacian team made a brilliant world cup campaign reaching the final match",
             "Google Chrome extensions are useful.",
             "Social Media apps leveraging AI incredibly",
             "Qatar 2022 FIFA world cup is played in winter"]
 
 
vectorizer = TfidfVectorizer(stop_words = 'english')
data = vectorizer.fit_transform(documents)
# print('data==>>]\n', type(data) , data)
 
true_k = 2
clustering_model = KMeans(n_clusters = true_k, 
                          init = 'k-means++',
                          max_iter = 300, n_init = 10)
cl = clustering_model.fit(data)
# pprint("cluster\n" , cl)
 
print("Top terms per cluster:")

sorted_centroids = clustering_model.cluster_centers_.argsort()[:, ::-1]
pprint(sorted_centroids)
terms = vectorizer.get_feature_names()

for i in range(true_k):
        print("Cluster %d:" % i, end='')
        for ind in sorted_centroids[i, :10]:
            print(' %s' % terms[ind], end='')
        print()
        print()
 
print()
print("Predictions of new documents")
 
new_doc = ["how to install Chrome"]
Y = vectorizer.transform(new_doc)
prediction = clustering_model.predict(Y)
print(prediction)
 
new_doc = ["UCL Final match is played in Madrid this year"]
Y = vectorizer.transform(new_doc)
prediction = clustering_model.predict(Y)
print(prediction)

# Top terms per cluster:
# Cluster 0: apps google funny camera extensions useful chrome driving face facebook
#
# Cluster 1: world cup young champions crowned french men qatar fifa played
#
# Predictions of new documents
# [0]
# [1]