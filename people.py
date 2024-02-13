#people
#name and age
#my name is and my age is
# for 5 people

class people:
      def __init__(self,name,age):
          self.name=name
          self.age=age
      def show(self):
         print(f"My name is {self.name}"
            f" and I am {self.age} years old ")
myperson=people( name="Wafula", age=24)
myperson.show()
myperson2=people( name="Claire", age=28)
myperson2.show()
myperson3=people( name="Beatrice", age=18)
myperson3.show()
myperson4=people( name="Wanjiru", age=12)
myperson4.show()
myperson5=people( name="Michael", age=13)
myperson5.show()

