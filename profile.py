import matplotlib.pyplot as plt
import numpy as np
import random

def randomizer(func):
  def wrapper(*args, **kwargs):
    random.seed()
    data = kwargs['data']
    length = len(data)
    for count in range(kwargs['num']):
      chosen = random.randint(0, length)
      print(data[chosen])
      func([x * 0.01 for x in range(length)], data[chosen], "X", "Temperature",
           "Temperature by X axis Distance", f"Y fixed at {round(chosen * 0.01, 3)}")
  return wrapper

@randomizer
def plotter(x, y, xlabel, ylabel, suptitle, title):
  plt.plot(x, y)
  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.suptitle(suptitle)
  plt.title(title)
  plt.show()


with open('heat_maps/heat_plot.600', 'r') as rf:
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
  plotter(data=data, num=10)
