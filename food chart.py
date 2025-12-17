food =[]
price=[]
total=0

while True:
    food_item = input("Enter food to buy:(q to quit): )")
    if food_item.lower() == "q":
        break
    else:
        price_item = float(input(f"Enter price of {food_item}:  $"))
        food.append(food_item)
        price.append(price_item)

        print("------YOUR CART------")
        for item in food:
            print(item)
        for price_item in price:
            total += price_item
print()
print(f" your Total is: ${total}")