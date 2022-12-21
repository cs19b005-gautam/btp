import gym
import gym_simplifiedtetris
import time

env = gym.make('simplifiedtetris-binary-v0')
obs = env.reset()

# Run 10 games of Tetris, selecting actions uniformly at random.
num_episodes = 0
while num_episodes < 100:
    env.render()
    action = env.action_space.sample()
    obs, rwd, done, info = env.step(action)
    print('Intermediary sleep')
    time.sleep(2)
    if done:
        print(f"Episode {num_episodes + 1} has terminated.")
        num_episodes += 1
        time.sleep(8)
        print('Long sleep')
        obs = env.reset()

env.close()