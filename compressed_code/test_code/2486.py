def solution():
    
    initial_pets = 16
    lost_pets = 6
    remaining_pets = initial_pets - lost_pets
    old_age_deaths = remaining_pets // 5
    final_pets = remaining_pets - old_age_deaths
    result = final_pets
    return result

print(solution())