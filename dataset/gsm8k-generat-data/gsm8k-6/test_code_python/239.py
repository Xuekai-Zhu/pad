def solution():
    # Calculate the total amount of money Frank has
    total_money = 7*1 + 4*5 + 2*10 + 1*20  # in dollars

    # Calculate the amount of money Frank spends on peanuts
    peanuts_cost = total_money - 4  # he has $4 in change after buying peanuts

    # Calculate the amount of peanuts he buys
    peanuts = peanuts_cost / 3  # peanuts cost $3 a pound

    # Calculate the average pounds of peanuts he eats per day
    average_pounds = peanuts / 7  # he eats them all in one week
    result = average_pounds
    return result

print(solution())