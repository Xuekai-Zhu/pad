def solution():
    old_animal_types = 5
    new_animal_types = 4
    time_to_see_each_type = 6
    total_time = old_animal_types + new_animal_types
    total_time_in_minutes = total_time * time_to_see_each_type
    result = total_time_in_minutes
    return result

print(solution())