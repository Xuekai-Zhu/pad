def solution():
    
    first_four_months_total = 30 * 4
    last_two_months_total = 24 * 2
    total_cost = first_four_months_total + last_two_months_total
    average_cost = total_cost / 6
    result = average_cost
    return result

print(solution())