def solution():
    """Mike is shopping at the mall. He needs to buy a shirt, a new wallet, and some food for the evening. The shirt costs a third of the value of the wallet. The wallet is $60 more than the cost of the food, on which Mike spent $30. How much did Mike spend that day on the shopping?"""
    # Define the cost of the food
    food_cost = 30

    # Calculate the cost of the wallet
    wallet_cost = food_cost + 60

    # Calculate the cost of the shirt
    shirt_cost = wallet_cost / 3

    # Calculate the total cost of the shopping
    total_cost = food_cost + shirt_cost + wallet_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())