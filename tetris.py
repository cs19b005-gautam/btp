from nes_py.wrappers import JoypadSpace
import gym_tetris
from gym_tetris.actions import SIMPLE_MOVEMENT

import time

env = gym_tetris.make('TetrisA-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)


total_reward = 0
temp =  None
done = True
done_cnt = 0
for step in range(5000):
    if done:
        done_cnt+=1
        # print('Inside Done Statement with done_cnt = ', done_cnt)
        # time.sleep(9)
        state = env.reset()
    # time.sleep(1.5)
    action = env.action_space.sample()
    state, reward, done, info = env.step(action)
    print(state[:,:,0].shape)
    env.render()
    # time.sleep(9)
    print('action = ', action)
    total_reward+=reward
    # print('Time Sleep Started...')
    # time.sleep(1.5) # 6 seconds
    # print("Time's Awake!!")
    print()
    print(info)
    print('done_cnt = ',done_cnt)
    temp = state
    # break

# type(state)   = <class 'numpy.ndarray'>
# state.shape   = (240, 256, 3) 
# type(action)  = <class 'int'>
# type(reward)  = <class 'float'>
# type(done)    = <class 'bool'>
# type(info)    = <class 'dict'>

print('done_cnt = ', done_cnt)

'''
  sample info   = {
                    'current_piece': 'Ld', 
                    'number_of_lines': 0, 
                    'score': 0, 
                    'next_piece': 'Td', 
                    'statistics': {'T': 0, 'J': 0, 'Z': 0, 'O': 0, 'S': 0, 'L': 1, 'I': 0}, 
                    'board_height': 0
                } 
'''

print()
print()
print(temp.shape)
print(type(temp))

env.close()