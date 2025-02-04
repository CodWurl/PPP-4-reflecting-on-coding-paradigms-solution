# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    print("R2 unit ran some repairs")
    self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
      super().__init__(max_speed, condition, price)
  
  def boost(self):
    print("Boosted speed by 2")
    self.max_speed *= 2
    
  def race_status(self):
      print(f"Anakin's max speed is {self.max_speed} - his pod condition is {self.condition}")
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)
  
  def flame_jet(self,other):
    print("flamed another pod")
    other.condition = "trashed"
    
anakins = AnakinsPod(2500, "new", 50_000_000)
sebublas = SebulbasPod(3500, "refurbished", 25_000_000)

anakins.race_status()
anakins.boost()
anakins.race_status()
sebublas.flame_jet(anakins)
anakins.race_status()
anakins.repair()
anakins.race_status()

 
'''
Make sure to answer the following prompts about your coding experience:


How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

# Encapsulation: It keeps max speed, condition, etc in the base class and extended classes use those base class attributes
# Abstraction: Abstracts away methods for indicating repair and setting initial values.
# Inheritance: Each pod inherits the condition and other aspects of the pod parent.
# Polymorphism: You can call the repair method on any decedent of pod


Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
This is appropriate use of OOP because each pod is an individual that descends from a base class that has 
built in functionality

How in particular did Object Oriented Programming assist in the solving of this problem?
See above --- using OOP you can create many additional pods without recreating all the mehtods
and properties of the first pod.

'''

