# gym_tetris package

- gym_tetris.action
- gym_tetris.make

# packages used for gym-tetris setting
- nes-py
- setuptools
- twine

# Action space in gym-tetris

``` 
MOVEMENT = [
    ['NOOP'], 
    ['A'], ['B'], ['right'], ['left'], ['down'],
    
    ['right', 'A'], ['right', 'B'],
    ['left', 'A'], ['left', 'B'],
    ['down', 'A'],['down', 'B'],
]
```
```
SIMPLE_MOVEMENT = [['NOOP'], ['A'], ['B'], ['right'], ['left'],['down']]
```