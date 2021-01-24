import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
  
  rw= RandomWalk()
  rw.fill_walk()
  
  point_numbers =list(range(rw.numpoints))
  
  plt.figure(dpi=128,figsize=(10,6))

  plt.scatter(rw.x_values,rw.y_values,s=1,c= point_numbers ,cmap = plt.cm.Reds)
  
  plt.scatter(0,0,c = "green",s=100)
  plt.scatter(rw.x_values[-1],rw.y_values[-1],s=100,c='green')
  
  
  plt.axes().get_xaxis().set_visible(False)
  plt.axes().get_yaxis().set_visible(False)
  plt.show()
  
  keep_running = input("Make another walk")
  if keep_running == "n":
    break
  