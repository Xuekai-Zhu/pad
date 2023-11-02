def solution():
    gold_value = 50  # Value of one gold coin
    silver_value = 25  # Value of one silver coin
    num_gold_coins = 3  # Number of gold coins
    num_silver_coins = 5  # Number of silver coins
    cash = 30  # Amount of cash in dollars

    # Calculate total value of gold coins
    gold_total = gold_value * num_gold_coins

    # Calculate total value of silver coins
    silver_total = silver_value * num_silver_coins

    # Calculate total amount of money
    total = gold_total + silver_total + cash
    result = total
    return result

print(solution())