def solution():
    # Calculate the cost of Ed's stay at the hotel
    night_cost = 1.5 * 6
    morning_cost = 2 * 4
    total_cost = night_cost + morning_cost

    # Calculate how much money Ed was left with
    remaining_money = 80 - total_cost
    result = remaining_money
    return result

print(solution())