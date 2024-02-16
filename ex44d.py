class Parent(object):

  def override(self):
    print("PARENT override()")
  
  def implicit(self):
    print("PARENT implicit()")
  
  def altered(self):
    print("PARENT altered()")

class Child(Parent):

  def override(self):
    print("CHILD override()")

  def altered(self):
    print("CHILD, BEFORE PARENT altered()")
    # super(Child, self).altered()
    super().altered() # 파이썬3 부터는 인수를 안 넣는 것을 권장한다고 함. 그래야 MRO(Method Resolution Order)가 더 잘 작동한다고.
    print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()