# Example of multiple inheritance:

class A:
   print("In class A: Grandparent")
   pass
class B:
   print("In class B: Grandparent")
class C (A, B):
   print("In class C: parent")
class D (A, B):
   print("In class D: parent")
class E (D, C):
   print("In class E: child")

print(E.__mro__) # Shows the MRO in reverse order (from the top to the bottom of the inheritance tree)

# Here, E inherits everything from its two parents, D and C, and they in turn inherit from their parent A, so E has everything from A, B, C and D. However, the order at the time of accessing an attribute or method using super(), for example, is from left to right and from the bottom to the top (refer to the OOP-rectangle.md). This is the way the Method Resolution Order (MRO) works in Python: using the C3 linearization algorithm, it travels all of the classes in the same abstraction level in the order they are declared (from left to right) and then it goes to the next level of abstraction (from bottom to top) and so on.
# ! However, you need to be careful with how do you declare multiple inheritance, because classes of the same level must have the same parent order for the MRO to work, since it supresses equal calls in the same order from different children. Otherwise, there will be a copy of the same class in the MRO, which is not allowed.
# For example, C and D have the same parent in the same order (A, B), so there won't be two copys of A and B in the MRO of E, but if you change the order of the parents in C and D, there will be two copys of A and B in the MRO of E, which is not allowed.