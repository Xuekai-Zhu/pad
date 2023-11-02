def solution():
    
    total_cost = 20
    chips_cost = 2 * 2
    chicken_cost = 8
    soda_cost = 1
    total_spent = chips_cost + chicken_cost + soda_cost
    apple_pie_cost = total_cost - total_spent
    result = apple_pie_cost
    return result

print(solution())