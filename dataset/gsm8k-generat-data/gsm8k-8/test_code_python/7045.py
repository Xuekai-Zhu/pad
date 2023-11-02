def solution():
    # Calculate the amount earned from vacuuming (2 hours * $5/hour * 2 times)
    vacuuming_money = 2 * 5 * 2

    # Calculate the amount earned from washing dishes (0.5 hours * $5/hour)
    dishes_money = 0.5 * 5

    # Calculate the amount of time spent cleaning the bathroom (3 times the amount spent washing dishes)
    bathroom_time = 3 * 0.5

    # Calculate the amount earned from cleaning the bathroom (bathroom_time * $5/hour)
    bathroom_money = bathroom_time * 5

    # Calculate the total amount earned
    total_money = vacuuming_money + dishes_money + bathroom_money

    result = total_money
    return result

print(solution())