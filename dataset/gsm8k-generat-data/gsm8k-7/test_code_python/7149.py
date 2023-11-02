def solution():
    wed_thu_fri_cost = 0.5 * 3  # cost of buying 3 editions
    sunday_cost = 2.0
    num_weeks = 8

    # Calculate the total cost of buying newspapers over 8 weeks
    total_cost = num_weeks * (wed_thu_fri_cost * 3 + sunday_cost)
    result = total_cost
    return result

print(solution())