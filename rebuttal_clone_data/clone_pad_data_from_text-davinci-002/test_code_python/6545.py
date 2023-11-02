def solution():
    machine_cost = 200
    discount = 20
    daily_cost = 3
    previous_coffee_cost = 4 * 2
    total_saved = daily_cost - previous_coffee_cost
    total_needed = machine_cost - discount
    number_of_days = total_needed / total_saved
    result = number_of_days
    
    return result

print(solution())