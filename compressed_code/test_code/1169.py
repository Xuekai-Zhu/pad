def solution():
    
    customers_per_hour = 10
    hours_worked = 8
    total_customers = customers_per_hour * hours_worked
    bonus_percentage = 0.2
    bonus_points = bonus_percentage * total_customers
    result = bonus_points
    return result

print(solution())