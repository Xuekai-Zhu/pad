def solution():
    # Calculate the number of sharks Pat can expect to see in 5 hours
    sharks_seen = 5 * 60 / 10  # he sees a shark about every 10 minutes

    # Calculate the total amount of money Pat can expect to make
    money_made = sharks_seen * 15

    # Calculate the cost of fuel for 5 hours
    fuel_cost = 50 * 5

    # Calculate the expected profit
    expected_profit = money_made - fuel_cost
    result = expected_profit
    return result

print(solution())