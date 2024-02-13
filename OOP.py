class fruits:
    def __init__(self,name,price,color):
        self.name=name
        self.price=price
        self.color=color
    def onyesha(self):
        print(f"My favourite fruit is {self.name}"
              f" which is colored {self.color}"
                 f" and it costs Ksh. {self.price}")

myobj=fruits(name="Apples",price=50,color="red")
myobj.onyesha()


