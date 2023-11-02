def solution():
    
    hours_per_lesson = 1.5
    cost_per_lesson = 30
    total_hours = 18
    number_of_lessons = total_hours / hours_per_lesson
    total_cost = number_of_lessons * cost_per_lesson
    result = total_cost
    return result

print(solution())