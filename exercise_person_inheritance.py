
# * Inheritance is a way to lend or borrow code from a class to another, so you don't have to write the same code again and again. It in consequence allows you to create a family of classes in which the children (derived classes) inherit attributes and methods from the parent(s) (base) class(es) that are in turn now part of them. Therefore, if you create an object of a derived class it will have all the attributes and methods of the parent class as well as of its own class.

# * super(Type, object_or_type = none) is a proxy object, i.e., a copy of the self() object of the base or parent class that lends or delegates method calls and attribute access to the object of Type (the instance of a child or derived class).

class Person:
   def __init__(self, age: int = 0, name: str = "Pepito") -> None:
      self.age: int = age # * Instance attributes: They are unique to each instance of a class
      self.name: str = name

   def greeting(self) -> None:
      print(self.name, "is greeting you!")
   
   def speak(self) -> None:
      print("Hello from", self.name)

   def is_older_than(self, person) -> bool:
      if (self.age > person.age):
         return True
      else:
         return False
   
   specie: str = "Homo Sapiens Sapiens Sapiens" # * Class attributes: Remain unchanged in every instance of the class

class Student(Person):
   def __init__(self, age: int = 0, name: str = "Pepito", ID: int = 0) -> None:
      super().__init__(age, name) 
      # ! You must call the bass class initializer in a subclass, since otherwise you won't have an instance of the bass class (super) to use in the subclass, so there wouldn't be inheritance
      self.id: int = ID
   def studying(self) -> None:
      self.speak()
      print(self.name, "is stu-dying 💀")

if __name__ == "__main__":
   Jesus = Person(age = 18, name = "Jesus")
   Jesus.greeting()

   user_name:str = str(input("Now insert your name please: "))
   user_age:int = int(input("and your age please: "))
   Other = Person(age = user_age, name = user_name)

   oldest: bool = Other.is_older_than(Jesus)
   if oldest == True:
      print("Congratulations {}! You are older than {}".format(Other.name, Jesus.name))
   else:
      print("{} is as old or older than you, {}!".format(Jesus.name, Other.name))

   student_oop: str = str(input("Please insert your name, student: "))
   student_age: int = int(input("your age as well please: "))
   student_id: int = int(input("and your student id: "))
   StudentOop = Student(age = student_age, name = student_oop, ID = student_id)
   StudentOop.studying()
