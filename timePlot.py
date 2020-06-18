import matplotlib.pyplot as plt

with open("times/time", "r") as rf:
  y = eval(rf.readline().replace('\n', ''))
  x = eval(rf.readline().replace('\n', ''))
  plt.plot(x, y, 'ro-')
  plt.xlabel("Number of Nodes")
  plt.ylabel("Simulation Time (ms)")
  plt.title("Number of Nodes by Simulation Time")
  plt.show()
