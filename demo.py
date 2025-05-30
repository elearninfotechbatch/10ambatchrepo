class vehicle:
  def intro(self):
    print("Vehicle")
  def speed(self):
    print("Speed:  Range 10-100kmph")
  
class bike(vehicle):
  def speed(self):
    print("Bike - 80kmph")
    
class car(vehicle):
  def speed(self):
    print("Car - 100kmph")
    
obj1=vehicle()
obj2=bike()
obj3=car()

obj1.intro()
obj1.speed()

obj2.speed()

obj3.speed()
