import numpy as np

patterns = {
    'vertical' : np.array([
        [0,1,0],
        [0,1,0],
        [0,1,0],
    ]),
    'horizontal' : np.array([
        [0,0,0],
        [1,1,1],
        [0,0,0],
    ]),
    'diagonal' : np.array([
        [1,0,0],
        [0,1,0],
        [0,0,1],
    ]),
}

X = np.stack([image.flatten()for image in patterns.values()])
Y = np.array(list(patterns.keys()))

print("X shape: ", X.shape)
print("Y shape: ", Y.shape)
print("X: ", X)
print("Y: ", Y)
print()
print("Labels: ", Y)
