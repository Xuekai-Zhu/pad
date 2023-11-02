def solution():
    current_lennon_age = 8
    years_in_future = 2
    
    # Calculate Lennon's age in the future
    future_lennon_age = current_lennon_age + years_in_future
    
    # Calculate Ophelia's age in the future based on the given ratio
    future_ophelia_age = 4 * future_lennon_age
    
    # Calculate Ophelia's current age
    current_ophelia_age = future_ophelia_age - years_in_future
    
    result = current_ophelia_age
    return result

print(solution())