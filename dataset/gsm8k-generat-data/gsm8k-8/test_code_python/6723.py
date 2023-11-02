def solution():
    # Calculate how many inches Bob's hair grew
    hair_growth = 36 - 6
    
    # Convert inches to months by dividing by growth rate
    months_to_grow = hair_growth / 0.5
    
    # Convert months to years by dividing by 12
    years_to_grow = months_to_grow / 12
    
    result = years_to_grow
    return result

print(solution())