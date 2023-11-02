def solution():
    # Calculate the number of oranges Timmy needs to buy to reach 400 calories
    oranges_needed = 400 / 80  # each orange has 80 calories
    # Round up to the nearest whole number because he can't buy a fraction of an orange
    oranges_needed = math.ceil(oranges_needed)

    # Calculate the cost of the oranges Timmy needs to buy
    cost = oranges_needed * 1.20

    # Calculate the amount of money Timmy will have left after buying the oranges he needs
    money_left = 10 - cost
    result = money_left
    return result

print(solution())