def solution():
    # Let x be the age of Markus's grandson
    x = 1
    
    # Calculate the age of Markus's son
    son_age = x * 2
    
    # Calculate the age of Markus
    markus_age = son_age * 2
    
    # Calculate the sum of their ages
    total_age = x + son_age + markus_age
    
    # Update x until the total_age equals 140
    while total_age != 140:
        x += 1
        son_age = x * 2
        markus_age = son_age * 2
        total_age = x + son_age + markus_age
        
    result = x
    
    return result

print(solution())