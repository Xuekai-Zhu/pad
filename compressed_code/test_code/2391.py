def solution():
    
    total_working_hours = 24 - 8
    cleaning_time = 4
    cooking_time = 2
    total_time_spent = cleaning_time + cooking_time
    crafting_and_tailoring_hours = (total_working_hours - total_time_spent) / 2
    crafting_hours = crafting_and_tailoring_hours
    result = crafting_hours
    return result

print(solution())