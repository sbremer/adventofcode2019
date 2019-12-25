import numpy as np
from matplotlib import pyplot as plt

import aoc

day = 8
lines = aoc.get_input(day)

x, y = 25, 6

image_all = np.array(list(lines[0])).astype(int).reshape((-1, y, x)).transpose()

zeros_min = x*y + 1
zeros_min_layer = -1

for layer in range(image_all.shape[2]):
    image = image_all[:, :, layer]
    zeros = (image == 0).sum()
    if zeros < zeros_min:
        zeros_min = zeros
        zeros_min_layer = layer

image = image_all[:, :, zeros_min_layer]

result = (image == 1).sum() * (image == 2).sum()

correct = aoc.submit(result, day)
print(f'Answer 1 correct: {correct}')

id_x, id_y = np.ogrid[0:x, 0:y]
id_non_2 = np.argmax(image_all != 2, axis=2)

# image = np.take(image_all, id_non_2)
image = image_all[id_x, id_y, id_non_2]
plt.imshow(image.transpose())

correct = aoc.submit('ZBJAB', day, 2)
print(f'Answer 2 correct: {correct}')
