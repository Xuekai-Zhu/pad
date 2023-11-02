def solution():
    
    current_animal_types = 5
    new_animal_types = 4
    minutes_per_animal_type = 6
    total_animal_types = current_animal_types + new_animal_types
    total_time = total_animal_types * minutes_per_animal_type
    result = total_time
    return result

print(solution())