# Create a dictionary named inventory 
inventory = {
    "Rice": 52.5,
    "Milk": 30.0,
    "Bread": 40.5,
    "Eggs": 75.0
}

# Create a list named cart with some items
cart=["Rice", "Milk", "Eggs"]
print(type(inventory))
print(type(cart))
print(type(inventory["Rice"]))

# Calculate total bill for items in cart

Total_bill=0

for item in cart:
    Total_bill=Total_bill+inventory[item]
print("Total bill:", Total_bill)

# Check if items in cart are available in inventory
for item in cart:
    if item in inventory:
        print(item,"available")
    else: 
        print(item,"not available")
    
# Create a set of unique items in cart
cart=["Rice", "Milk", "Eggs", "Rice"]
unique_cart=set(cart)
print(unique_cart)

# Create a tuple of product categories
product_category=("fruits","dairy","bakery")
print(product_category)
print(type(product_category))
    
# Add an item with None as the price and show its type.

inventory = {
    "Rice": 52.5,
    "Milk": 30.0,
    "Bread": 40.5,
    "Eggs": 75.0,
    "Sugar":None
}
print(inventory)
print(type(inventory["Sugar"]))

# Use a boolean variable to check if total bill exceeds a certain amount and print the result.
is_discount_applied=False

if Total_bill > 100:
    is_discount_applied=True
    print("Discount applied:", is_discount_applied)