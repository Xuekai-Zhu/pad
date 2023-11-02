def solution():
    # Calculate the total amount of money Marj has
    total_money = (2 * 20) + (3 * 5) + 4.5  # Two $20 bills, three $5 bills, and $4.50 in coins

    # Calculate the amount of money she will spend on the cake
    cake_cost = 17.5

    # Calculate how much money will be left in her wallet
    money_left = total_money - cake_cost
    result = money_left
    return result

print(solution())