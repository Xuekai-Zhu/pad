def solution():
    
    total_hours = 24
    cleaning_time = 4
    cooking_time = 2
    sleeping_time = 8
    working_time = total_hours - cleaning_time - cooking_time - sleeping_time
    crafting_time = working_time / 2
    result = crafting_time
    return result

print(solution())