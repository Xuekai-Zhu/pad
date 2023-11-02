def solution():
    
    first_day_customers = 100
    second_day_customers = first_day_customers + 50
    total_customers = 500
    third_day_customers = total_customers - first_day_customers - second_day_customers
    result = third_day_customers
    return result

print(solution())