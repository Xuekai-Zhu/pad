def solution():
    cost_per_lesson = 30
    duration_per_lesson = 1.5
    total_duration = 18
    
    # Calculate the total number of lessons
    total_lessons = total_duration / duration_per_lesson
    
    # Calculate the total cost
    total_cost = total_lessons * cost_per_lesson
    
    result = total_cost
    return result

print(solution())