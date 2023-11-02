def solution():
    # Calculate the total amount of crab meat used per week
    crab_meat_weekly = 40 * 1.5 * 4

    # Calculate the total cost of crab meat per week
    crab_meat_cost_weekly = crab_meat_weekly * 8

    # Calculate the number of days that Johnny is open per week
    open_days = 7 - 3

    # Calculate the total cost of crab meat per open day
    crab_meat_cost_open_day = crab_meat_cost_weekly / open_days

    result = crab_meat_cost_open_day
    return result

print(solution())