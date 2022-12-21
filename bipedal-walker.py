import gym
env = gym.make("BipedalWalker-v3", hardcore=True)

for step in range(200):
    if done:
        state = env.reset()
    # time.sleep(1.5)
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)
    print(state.shape)
    env.render()
    # print('Time Sleep Started...')
    # time.sleep(1.5) # 6 seconds
    # print("Time's Awake!!")
    print()
    print(info)
    temp = state
    # break

env.close()