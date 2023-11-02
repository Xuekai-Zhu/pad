def solution():
    """Jim and his Cousin are out at a restaurant. They each order a cheeseburger and milkshake. They also split an order to cheese fries. A cheeseburger is $3. A milkshake is $5. Cheese fries are $8. They spend 80% of their combined money. If Jim brought $20 how much did his cousin bring?"""
    # Define the cost of each menu item
    BURGER_PRICE = 3
    SHAKE_PRICE = 5
    FRIES_PRICE = 8

    # Define the number of each menu item ordered
    burgers = 2
    shakes = 2
    fries = 1

    # Calculate the total cost of the meal
    total_cost = burgers * BURGER_PRICE + shakes * SHAKE_PRICE + fries * FRIES_PRICE

    # Calculate the amount of money Jim and his cousin spent
    spent_money = total_cost * 0.8

    # Calculate the amount of money Jim spent
    jim_money = 20

    # Calculate the amount of money Jim's cousin spent
    cousin_money = spent_money - jim_money

    # Display the amount of money Jim's cousin spent
    result = cousin_money
    return result

print(solution())