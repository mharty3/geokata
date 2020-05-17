import numpy as np
from scipy.spatial import cKDTree

tree = cKDTree(boreholes_list)

def tree_mean_distance_between_boreholes(tree):
    """Calculate the mean distance between all boreholes stored in a kd-tree to the nearest integer"""
    
    distance_matrix = tree.sparse_distance_matrix(tree, np.inf).todense()
    distance_matrix = np.round(distance_matrix)
    mean_dist = distance_matrix[distance_matrix > 0].mean()
    
    return mean_dist.round()


def clump_count(tree):
    k = tree.n / 5 
    clump_dist = tree_mean_distance_between_boreholes(tree) / 4  # m/4
    
    dist, ind = tree.query(tree.data, k=k)
    mask = dist[:, 1:].mean(axis=1) < clump_dist
    
    return mask.sum()