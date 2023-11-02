def solution():
    # Calculate the cost of staying last night
    cost_last_night = 1.5 * 6  # $1.50 per hour, 6 hours

    # Calculate the cost of staying this morning
    cost_this_morning = 2 * 4  # $2 per hour, 4 hours

    # Calculate the total cost of staying at the hotel
    total_cost = cost_last_night + cost_this_morning

    # Calculate how much money Ed is left with
    money_left = 80 - total_cost
    result = money_left
    return result

print(solution())