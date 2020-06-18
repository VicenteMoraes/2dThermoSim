import matplotlib.pyplot as plt
import numpy as np
import os

files = os.listdir("heat_maps")
file = files[-1]
size = int(file.split(".")[-1])

with open(f'heat_maps/{file}', "r") as rf:
  data = rf.readlines()
  data = "".join(data) \
           .replace('\n', '') \
           .replace("(", "[") \
           .replace(")", "]") \
           .replace(" ", ",") \
           .replace("NIL", "0") \
           .replace(",,", ",")
  data = eval(data)
  data = np.asarray(data)
  #map = plt.colors.Colormap('hot')
  plt.imshow(data, cmap='hot_r', interpolation='nearest', vmin=0, vmax=101, extent=[0, 3, 0, 3])
  plt.ylabel("Y")
  plt.xlabel("X")
  plt.suptitle("L shaped Difference Simulation")
  plt.title(f'Node Count: {size ** 2}')
  plt.colorbar(label="Temperature")
  plt.show()
