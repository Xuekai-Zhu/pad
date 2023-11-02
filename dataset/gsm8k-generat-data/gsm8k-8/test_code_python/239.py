def solution():
    # Calculate total amount of money Frank has
    total_money = 7*1 + 4*5 + 2*10 + 1*20

    # Calculate the amount spent on peanuts
    peanuts_cost = total_money - 4

    # Calculate the amount of peanuts bought
    peanuts_weight = peanuts_cost / 3

    # Calculate the average amount of peanuts eaten per day
    average_peanuts_per_day = peanuts_weight / 7

    result = average_peanuts_per_day
    return result

print(solution())