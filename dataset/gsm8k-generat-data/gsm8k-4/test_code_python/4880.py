def solution():
    """Jim and his Cousin are out at a restaurant. They each order a cheeseburger and milkshake. They also split an order to cheese fries. A cheeseburger is $3. A milkshake is $5. Cheese fries are $8. They spend 80% of their combined money. If Jim brought $20 how much did his cousin bring?"""
    # Define the prices of cheeseburger, milkshake, and cheese fries
    cheeseburger_price = 3
    milkshake_price = 5
    cheese_fries_price = 8

    # Calculate the total cost of the food
    food_cost = (2 * cheeseburger_price) + (2 * milkshake_price) + cheese_fries_price

    # Calculate the total amount of money spent
    total_spent = food_cost / 0.8

    # Calculate how much money Jim's cousin brought
    cousin_money = total_spent - 20

    # return the result
    result = cousin_money
    return result

print(solution())