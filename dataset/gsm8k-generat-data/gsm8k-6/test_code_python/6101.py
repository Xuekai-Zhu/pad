def solution():
    # Calculate the remaining amount of money Cary needs to save
    remaining_money = 120 - 30  # the shoes cost $120 and he has already saved $30

    # Calculate how much money Cary can earn each weekend
    money_earned_per_weekend = 5 * 3  # he mows 3 lawns each weekend and earns $5 for each

    # Calculate how many more weekends Cary needs to mow lawns to save enough money
    weekends_needed = (remaining_money // money_earned_per_weekend) + 1  # add 1 to round up

    result = weekends_needed
    return result

print(solution())