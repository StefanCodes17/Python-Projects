import numpy as np


# Reward matrix
R = np.matrix([[-1, -1, -1, -1, 0, -1],
               [-1, -1, -1, 0, -1, 100],
               [-1, -1, -1, 0, -1, -1],
               [-1, 0, 0, -1, 0, -1],
               [-1, 0, 0, -1, -1, 100],
               [-1, 0, -1, -1, 0, 100]])
print("R matrix \n", R)

# Q matrix
Q = np.matrix(np.zeros([6, 6]))
print("Q matrix \n", Q)

# Gamma (Learning parameter for exploitation vs exploration)
gamma = 0.8

# Initial State (Chosen at random for starting room)
initial_state = np.random.randint(0, 5)
print("Starting room:", initial_state)


def available_actions(state):
    ''' 
    @param state This refers to the state or room that agent is starting in
    @return Returns all possible actions of agent from input state
    '''
    current_state_row = R[state]
    av_actions = np.where(current_state_row >= 0)[1]
    return av_actions


available_act = available_actions(initial_state)


def sample_next_action(available_actions_set):
    '''
    @param available_actions_set A list of available valid actions
    @return Returns a random sample action from the available actions
    '''
    next_action = int(np.random.choice(available_actions_set, 1))
    return next_action


action = sample_next_action(available_act)
#print("Sample action", action)


def update(current_state, action, gamma):
    '''
    @param current_state The current state chosen
           action The chosen random action
           gamma  Explore vs exploit choice
    '''
    max_index = np.where(Q[action] == np.max(Q[action]))[1]
    if(max_index.shape[0] > 1):
        max_index = int(np.random.choice(max_index, size=1))
    else:
        max_index = int(max_index)
    max_value = Q[action, max_index]

    # Q Learning formula
    Q[current_state, action] = R[current_state, action] + (gamma * max_value)


update(initial_state, action, gamma)

# Training phase
for i in range(10000):
    current_state = np.random.randint(0, int(Q.shape[0]))
    available_act = available_actions(current_state)
    action = sample_next_action(available_act)
    update(current_state, action, gamma)

# Normalize the trained

print("Trained Q matrix:")
print(Q / np.max(Q) * 100)

# Goal state = 5
# Calculate the best policy
current_state = 2
steps = [current_state]

while current_state != 5:
    next_step_index = np.where(Q[current_state] == np.max(Q[action]))[1]
    if(next_step_index.shape[0] > 1):
        next_step_index = int(np.random.choice(next_step_index, size=1))
    else:
        next_step_index = int(next_step_index)

    steps.append(next_step_index)
    current_state = next_step_index

print("Selected path")
print(steps)
