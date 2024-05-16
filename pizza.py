
print("A Pizza Company")

price = 0.00
topping_price = 0.75
toppings = 0.00

size = input("what size pizza would you like S,M,L")

if size =="S":
    price = 7.50
if size =="M":
    price = 10.00
if size =="L":
    price = 13.00


print("Price of your pizza is {}".format(price,))



size = input("what toppings would you like Donner,Magherita,Pepproni")

if size =="Donner":
    toppings += 1
if size =="Magjerita":
    toppings += 1
if size =="Pepporoni":
    toppings += 1

print("Price of your topping is {}".format(toppings*topping_price,))
