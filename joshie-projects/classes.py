class item():
    def __init__(self, gardget,price,discount):
        self.gardget = gardget
        self.price = price
        self.discount = discount
    def minus(self,x,y):
        return x-y    
       
item1 = item("phone",90,10)
print(item1.minus(item1.price,item1.discount))
item2 = item("laptop",90,37)
print(item2.minus(item2.price , item2.discount))


print(item2.minus(13 ,6))