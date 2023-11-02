def solution():
    # Calculate the number of sharks Pat will see in 5 hours
    sharks_seen = 5 * 60 / 10  # Pat is on shark hunt for 5 hours, and he sees a shark every 10 minutes

    # Calculate the expected profit from shark photography
    profit = sharks_seen * 15  # Pat earns $15 for every photo he takes

    # Calculate the cost of fuel for the boat
    fuel_cost = 50 * 5  # Pat's boat fuel costs $50 an hour, and he shark hunts for 5 hours

    # Calculate the total profit after deducting fuel cost
    total_profit = profit - fuel_cost
    result = total_profit
    return result

print(solution())