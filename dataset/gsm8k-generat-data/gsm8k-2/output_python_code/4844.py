def solution():
    """Mike is shopping at the mall. He needs to buy a shirt, a new wallet, and some food for the evening. The shirt costs a third of the value of the wallet. The wallet is $60 more than the cost of the food, on which Mike spent $30. How much did Mike spend that day on the shopping?"""
    food_cost = 30
    wallet_cost = food_cost + 60
    shirt_cost = wallet_cost / 3
    total_cost = food_cost + wallet_cost + shirt_cost
    result = total_cost
    return result

print(solution())