from random import choice

class RandomWalk():
  
  def __init__(self,num_points= 50000):
  
    
    self.numpoints = num_points
  
    self.x_values= [0]
    self.y_values= [0]
    
    
    
  def get_step_x(self):
    
    x_direction= choice([-1,1])
    x_distance =choice([0,1,2,3,4])
    x_step1 = x_direction * x_distance
    return x_step1
    
  def get_step_y(self):
    y_direction= choice([-1,1])
    y_distance =choice([0,1,2,3,4])
    y_step1 = y_direction * y_distance
    return y_step1
    
     
  
    
    
  def fill_walk(self):
    while len(self.x_values) < self.numpoints:
      
      x_step = get_step_x()
      
      
      y_step = get_step_y()
      
      if x_step == 0 and y_step == 0:
        continue
      
      next_x = self.x_values[-1] + x_step
      next_y = self.y_values[-1] + y_step
    
      self.x_values.append(next_x)
      self.y_values.append(next_y)