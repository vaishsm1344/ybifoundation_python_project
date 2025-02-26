#Define the menu of restaurant
menu={
    'Pizza':40,
    'Pasta':35,
    'Burger':50,
    'Salad':25,
    'Coffee':30,
    }

#Greet
print("Welcome to HideOut Restaurant")
print("Pizza: Rs40\nPasta: Rs35\nBurger: Rs50\nSalad: Rs25\nCoffee: Rs30")

order_total=0
#30+25=55

item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total+=menu[item_1]#0+50
    print("Your item {item_1} has been added to your order")
    
else:
    print("Ordered item {item_1} is not available yet!")

another_order=input("(Do you want to add another item? (Yes/No)")
if another_order=="Yes":
    item_2=input("Enter the name of the second item=")
    if item_2 in menu:
        order_total+=menu[item_2]
        print("Item {item_2} has been added to order")
    else:
        print("Ordered item {item_2} is not available!")

print("The total amount of items to pay is",order_total)
print("Thank You Visit Again")



    
