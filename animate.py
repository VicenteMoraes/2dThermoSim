import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def animate(i):
  ax.imshow(data_list[i], cmap='hot_r', interpolation='nearest', vmin=0, vmax=101, extent=[0, 3, 0, 3])

def get_data(i):
  with open(f"animation/{i}", "r") as rf:
    data = rf.readlines()
    data = "".join(data) \
             .replace('\n', '') \
             .replace("(", "[") \
             .replace(")", "]") \
             .replace(" ", ",") \
             .replace("NIL", "0") \
             .replace(",,", ",")
    data = eval(data)
    print(i)
    return np.asarray(data)

data_list = [get_data(i) for i in range(720)]
fig, ax = plt.subplots()
ax.set(title="L shaped Difference Simulation",
       xlabel="X", ylabel="Y")
img = ax.imshow(data_list[0], cmap='hot_r', interpolation='nearest', vmin=0, vmax=101,
                extent=[0, 3, 0, 3])
fig.colorbar(img, label="Temperature")
animated = FuncAnimation(fig, animate, frames=720)
animated.save("animation.mp4", fps=24)
# plt.draw()
# plt.show()
