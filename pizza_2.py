
print("A Pizza Company")

# Variables

price = 0.00


topping_price = 0.75
toppings = 0.00
delivery_fee =1.50
total_cost=0.00
total_price=0.00


# funtions
def get_pizza_size():
    price=0.00

    size = input("what size pizza would you like S,M,L")

    if size =="S":
       price += 7.50
    elif size =="M":
       price += 10.00
    elif size =="L":
       price += 13.00

    return price








# code

   

price = get_pizza_size()

print("Price of your pizza is {}".format(price,))    

size = input("what toppings would you like Donner,Magherita,Pepproni")

if size =="Donner":
    toppings += 1
elif size =="Magjerita":
    toppings += 1
elif size =="Pepporoni":
    toppings += 1

print("Price of your topping is {}".format(toppings*topping_price,))


size = input("Would u like it to be delivered yes,no")

if size =="yes":
    price += 1.50
elif size =="no":
    price += 0.00

    
#price=format(price,'.2f')
#print('\xA3' + price)

total_price=price+(toppings*topping_price)

txt = "For only \xA3{price:.2f} pounds"

print(txt.format(price = total_price))
