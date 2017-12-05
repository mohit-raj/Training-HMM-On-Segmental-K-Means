
import pandas as pd
import numpy as np
from viterbi import Viterbi

from random import randrange

def get_segments (fileName, T = 10, N = 5):
    # fileName = '../data/day.csv'
    data = pd.read_csv(fileName)
    data.head()

    data = data[['temp', 'atemp', 'hum', 'windspeed']]
    data = data[:-1]

    # Define the w and T
    # T = 10
    w = data.shape[0] // T

    # N is number of states
    # N = 5

    print('w, T = ', w, T)
    print('N = ', N)

    # Split the data into a wxT numpy matrix
    sequences = data.values
    sequences = sequences.reshape(w, T, data.shape[1])

    return sequences

def cluster_k_means (segments):
    states = [[randrange(0, sequences.shape[0]*sequences.shape[1])] for state in range(0, N)]

    centroid_of_states = [sequences[x[0]//T][x[0]%T] for x in states]

    assigned_states = np.array(np.zeros((w, T)))
    for i in range(1, N+1):
        x = states[i-1][0] // T
        y = states[i-1][0] % T
        assigned_states[x][y] = i

    for i in range(0, w):
        for j in range(0, T):
            if assigned_states[i][j] == 0:
                
                min_dist = np.linalg.norm(centroid_of_states[0] - sequences[i][j])
                min_idx = 0
                for k in range(1, N):
                    dist_from_centroid = np.linalg.norm(centroid_of_states[k] - sequences[i][j])
                    if min_dist > dist_from_centroid:
                        min_dist = dist_from_centroid
                        min_idx = k
                
                state_idx = min_idx
                
                centroid_of_states[state_idx] = (centroid_of_states[state_idx] * len(states[state_idx]) + sequences[i][j]) / (len(states[state_idx]) + 1)
                states[state_idx].append((i*T + j))
                assigned_states[i][j] = state_idx + 1

def get_init_probability ():
    # Calculate initial probabilities
    pi_vector = [0 for i in range(0, N)]

    observations_all, counts_total = np.unique(df.values, axis=0, return_counts=True)

    counts_o1 = 0    
    for i in range(0, w):
        O1 = sequences[i][0]
        
        for state in states:
            state_vector = [sequences[idx // T][idx % T] for idx in state]
            
            observations, counts = np.unique(state_vector, axis=0, return_counts=True)
            idx = np.where(np.all(observations == O1, axis=1))
            
            if len(idx[0]) != 0:
                pi_vector[states.index(state)] += counts[idx[0][0]]

        idx = np.where(np.all(observations_all == O1, axis=1))
        counts_o1 += counts_total[idx[0][0]]

    pi_vector = pi_vector / counts_o1

def get_a_matrix ():
    # Calculate transition probabilities
    a_matrix = [[0 for i in range(0, N)] for j in range(0, N)]

    for i in range(0, N):
        for j in range(0, N):
            denominator = 0
            numerator = 0
            for k in range(0, w):
                for t in range(0, T-1):
                    if assigned_states[k][t] == i+1:
                        denominator += 1
                        if assigned_states[k][t+1] == j+1:
                            numerator += 1

            a_matrix[i][j] = numerator / denominator

def get_mean ():
    mean_vector = np.zeros((N, 4))
    for i in range(0, N):
        state_vector = [sequences[idx // T][idx % T] for idx in states[i]]
        mean_vector[i] = np.sum(state_vector, axis=0) / len(state)

def get_covariance ():
    # Co variance
    covariance_matrix = [None for i in range(0, N)]

    for i in range(0, N):
        state_vector = [sequences[idx // T][idx % T] for idx in states[i]]
        x = state_vector - mean_vector[i]
        
        covariance_matrix[i] = np.zeros((df.shape[1], df.shape[1]))
        for x_one in x:
            covariance_matrix[i] += x_one.T * x_one 
        covariance_matrix[i] /= len(states[i])

def get_emmision_probability ():
    # Emmision probability
    b = np.zeros((w, N, T))

    D = df.shape[1]

    for k in range(0, w):
        for i in range(0, N):
            for t in range(0, T):
                x = sequences[k][t].reshape(1, sequences[k][t].shape[0])
                y = mean_vector[i].reshape(1, mean_vector[i].shape[0])
                b[k][i][t] = (1 / (((2 * np.pi) ** (D / 2)) * (np.linalg.norm(covariance_matrix[i]) ** 0.5))) * np.exp(-0.5 * np.matmul(np.matmul((x - y), np.linalg.pinv(covariance_matrix[i])), (x - y).T))
