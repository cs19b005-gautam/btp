import gym
import time
import numpy as np
import policy
from utils import preprocess_sample_states as pre, get_pairs as pairs, get_mean_covariance_matrix
env_name = 'LunarLander-v2'
env = gym.make(env_name)
env.reset()


print('state space = ', env.observation_space)
print('action space = ', env.action_space)

# sample_states = pre(env_name)
# sample_state_action_pairs = pairs(sample_states)
# mean, cov = get_mean_covariance_matrix(sample_state_action_pairs)

tmp = int(input())
if(tmp==1):
    time.sleep(4)
    # exit

# Policy = policy.Policy(cov)

# print(type(cov), ' : ', cov.shape)
# print(type(mean), ' : ', mean.shape)

print('Rendering the environment...')
total_reward = 0
for _ in range(300):
    env.render()
    time.sleep(0.05)
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    total_reward+=reward
    if done:
        print("Total episodes = ", _+1, ' : reward = ', total_reward)
        break

env.reset()