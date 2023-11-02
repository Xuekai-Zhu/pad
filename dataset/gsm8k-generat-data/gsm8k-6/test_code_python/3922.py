def solution():
    # Calculate the current monthly production rate
    current_production_rate = 100  
    # Calculate the total number of cars needed to reach the target
    total_cars_needed = 1800  
    # Calculate the number of additional cars needed per month
    additional_cars = (total_cars_needed / 12) - current_production_rate  
    result = additional_cars
    return result

print(solution())