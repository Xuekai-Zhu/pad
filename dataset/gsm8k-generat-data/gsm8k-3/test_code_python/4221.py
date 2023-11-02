def solution():
    """John goes to the market with €100. He buys a roast for €17 and vegetables for €11. How much money does he have left?"""
    # Define the initial amount of money John has
    initial_money = 100

    # Define the cost of the roast and vegetables
    roast_cost = 17
    vegetable_cost = 11

    # Calculate the total cost of the shopping
    total_cost = roast_cost + vegetable_cost

    # Calculate the money left after shopping
    money_left = initial_money - total_cost

    # Display the money John has left
    result = money_left
    return result

print(solution())