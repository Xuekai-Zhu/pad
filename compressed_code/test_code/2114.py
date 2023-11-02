def solution():
    
    lesson_length = 1 
    lesson_frequency = 1 
    cost_per_half_hour = 10
    total_cost_per_lesson = cost_per_half_hour * 2 * lesson_length
    total_lessons = 5
    total_cost = total_cost_per_lesson * total_lessons * lesson_frequency
    
    result = total_cost
    return result

print(solution())