def solution():
    # Calculate the cost of staying at the hotel last night
    last_night_cost = 6 * 1.5

    # Calculate the cost of staying at the hotel this morning
    this_morning_cost = 4 * 2

    # Calculate the total cost of Ed's stay at the hotel
    total_cost = last_night_cost + this_morning_cost

    # Calculate how much money Ed has left after paying for his hotel stay
    money_left = 80 - total_cost
    result = money_left
    return result

print(solution())