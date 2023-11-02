def solution():
    # Calculate the cost of the wallet
    cost_of_food = 30  # Mike spent $30 on the food
    cost_of_wallet = cost_of_food + 60  # The wallet costs $60 more than the food
    # Calculate the cost of the shirt
    cost_of_shirt = cost_of_wallet / 3  # The shirt costs a third of the value of the wallet

    # Calculate the total cost of the shopping
    total_cost = cost_of_shirt + cost_of_wallet + cost_of_food
    result = total_cost
    return result

print(solution())