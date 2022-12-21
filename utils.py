import gym 
import numpy as np
env = None

def preprocess_sample_states(env_name):
    print('Preprocessing ...')
    env = gym.make(env_name)
    sample_states = []
    state = env.reset()
    sample_states.append(state)
    for _ in range(10000):
        for epoch in range(200):
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            sample_states.append(observation)
            if done:
                state = env.reset()
                sample_states.append(state)
                break
        if((_+1)%1000==0):
            print('Preprocessed ', (_+1)/100, '%')
    return sample_states

def get_pairs(sample_states):
    import numpy as np
    state_action_pairs = []
    for state in sample_states:
        state_action_pairs.append(np.append(state, np.random.randint(4)))
    return state_action_pairs

def get_mean_covariance_matrix(sample_state_action_pairs):
    mean = np.zeros(9)
    mean[-1] = 1.5
    np_cov = np.stack(sample_state_action_pairs, axis=1)
    cov = np.cov(np_cov)
    return mean, cov