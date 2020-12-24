import numpy as np


# Reward matrix
R = np.matrix([[-1, -1, -1, -1, 0, -1],
               [-1, -1, -1, 0, -1, 100],
               [-1, -1, -1, 0, -1, -1],
               [-1, 0, 0, -1, 0, -1],
               [-1, 0, 0, -1, -1, 100],
               [-1, 0, -1, -1, 0, 100]])
print(R)

# Q matrix
Q = np.matrix(np.zeros([6, 6]))
print(Q)

# Gamma (Learning parameter for exploitation vs exploration)
gamma = 0.8

# Initial State (Chosen at random for starting room)
initial_state = 1  # rand.randint(1, 5)


def available_actions(state):
    ''' 
    @param state This refers to the state or room that agent is starting in
    return Returns all possible actions of agent from input state
    '''
    current_state_row = R[state]
    av_actions = np.where(current_state_row >= 0)[1]
    return av_actions


available_act = available_actions(initial_state)
