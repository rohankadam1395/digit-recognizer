import numpy as np

vertical = np.array([
    [0,1,0],
    [0,1,0],
    [0,1,0],
])

horizontal = np.array([
    [0,0,0],
    [1,1,1],
    [0,0,0],
])

diagonal = np.array([
    [1,0,0],
    [0,1,0],
    [0,0,1],
])

for name, image in [('verical',vertical),('horizontal',horizontal),('diagonal',diagonal)]:
    print(name)
    print(image)
    print("flattened: ", image.flatten())
    print()


