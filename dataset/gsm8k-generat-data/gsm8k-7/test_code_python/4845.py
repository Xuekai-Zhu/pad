def solution():
    food_cost = 30

    # Calculate the cost of the wallet
    wallet_cost = food_cost + 60

    # Calculate the cost of the shirt
    shirt_cost = wallet_cost / 3

    # Calculate the total cost of the shopping
    total_cost = food_cost + wallet_cost + shirt_cost
    result = total_cost
    return result

print(solution())