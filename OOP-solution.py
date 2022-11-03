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
    self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
      super().__init__(max_speed, condition, price)
  
  def boost(self):
    self.max_speed *= 2
    
  def race_status(self):
      print(f"Anakin's max speed is {self.max_speed} - his pod condition is {self.condition}")
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)
  
  def flame_jet(self,other):
    other.condition = "trashed"
    
anakins = AnakinsPod(2500, "new", 50_000_000)
sebublas = SebulbasPod(3500, "refurbished", 25_000_000)

anakins.race_status()
anakins.boost()
anakins.race_status()
sebublas.flame_jet(anakins)
anakins.race_status()

 
'''
Make sure to answer the following prompts about your coding experience:


How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)

 Encapsulation: The Podracer class is encapsulated by the AnakinsPod and SebulbasPod classes. 
# The classes themselves are examples of encapsulation because they hold data and methods that are related to each other.
# Abstraction: The AnakinsPod and SebulbasPod classes inherit the attributes and methods of the Podracer class. 
# This hides the implementation details of the Podracer class from the user.
# Inheritance: We can see inheritance in the AnakinsPod and SebulbasPod classes because we resuse the code from the Podracer class without rewriting it.
# Polymorphism: We dont use polymorphism in this solution, but we could have used it to create a method that would work for both classes.


Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?

How in particular did Object Oriented Programming assist in the solving of this problem?

'''

