def find_all_distances(ds,distance_type='euclidean'):
    D = distance.cdist(ds, ds, 'euclidean')

def Davies_Bouldin_index(ds, labels):
    n , d = ds.shape
    cluster_labels  = np.unique(labels)
    cluster_labels = cluster_labels.flatten()[cluster_labels!=-1] #removes the noise
    number_of_clusters = cluster_labels.shape[0]
    centers = np.zeros((number_of_clusters,d))
    internal_dist = np.zeros(number_of_clusters)

    for i in cluster_labels:
        cluster_points = ds[labels==i]
        centers[i] = np.average(cluster_points, axis = 0)
        internal_dist[i] = np.average(find_all_distances(cluster_points))
    DB = 0
    for i in cluster_labels:
        max_ratio = 0
        for j in cluster_labels:
            if i==j:
                continue
            ratio = (internal_dist[i]+internal_dist[j])/(np.linalg.norm(centers[i]-centers[j]))
            if ratio> max_ratio:
                max_ratio = ratio
        DB+= max_ratio
    DB /= number_of_clusters 
    noise = np.count_nonzero([labels==i]) 

    return DB
