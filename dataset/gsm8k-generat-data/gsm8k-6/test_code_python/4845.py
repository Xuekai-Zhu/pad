def solution():
    # Calculate the cost of the wallet and the shirt
    food_cost = 30  # cost of the food
    wallet_cost = food_cost + 60  # wallet costs $60 more than the food
    shirt_cost = wallet_cost / 3  # shirt costs a third of the value of the wallet

    # Calculate the total cost of shopping
    total_cost = food_cost + wallet_cost + shirt_cost
    result = total_cost
    return result

print(solution())