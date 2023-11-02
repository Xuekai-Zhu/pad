def solution():
    cost_per_bottle = 50.00  # The cost of the perfume bottle they want to buy
    christian_savings = 5.00  # The amount Christian has saved up
    sue_savings = 7.00  # The amount Sue has saved up
    christian_earned = 4 * 5.00  # Christian earned $5.00 for mowing each of the 4 neighbors' yards
    sue_earned = 6 * 2.00  # Sue earned $2.00 for walking each of the 6 dogs

    # Calculate the total amount of money Christian and Sue have
    total_money = christian_savings + sue_savings + christian_earned + sue_earned

    # Calculate how much more money they need to make to buy the perfume bottle
    remaining_money = cost_per_bottle - total_money
    result = remaining_money
    return result

print(solution())