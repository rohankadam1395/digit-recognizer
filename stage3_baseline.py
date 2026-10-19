import numpy as np

prototypes = {
    "vertical" : np.array([
        [0,1,0,0,1,0,0,1,0],
    ]),
    "horizontal" : np.array([
        [0,0,0,1,1,1,0,0,0],
    ]),
    "diagonal" : np.array([
        [1,0,0,0,1,0,0,0,1],
    ]),
}

def predict(image_vector):
    distances = {
        label : np.sum(image_vector != prototype)
        for label, prototype in prototypes.items()
    }

    predicted_label = min(distances, key=distances.get)
    return predicted_label,distances


# test_image = np.array([
#     [0,1,0],
#     [0,1,0],
#     [0,1,0],
# ]).flatten()

# test_image = np.array([
#     [1,0,0],
#     [0,1,0],
#     [0,0,1],
# ]).flatten()

test_image = np.array([
    [0,0,0],
    [1,1,1],
    [0,0,0],
]).flatten()

label, distances = predict(test_image)
print("Distances: ", distances)
print("Predicted label: ", label)