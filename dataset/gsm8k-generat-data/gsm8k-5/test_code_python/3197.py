def solution():
    initial_pets = 16  # Anthony has 16 pets initially
    lost_pets = 6  # Anthony loses 6 pets
    remaining_pets = initial_pets - lost_pets  # Anthony has this many pets left after losing 6 pets
    
    # Calculate the number of pets that died from old age
    old_age_deaths = remaining_pets // 5  # 1/5 of Anthony's remaining pets die from old age
    
    # Subtract the pets that died from old age from the remaining pets
    remaining_pets -= old_age_deaths
    
    result = remaining_pets
    return result

print(solution())