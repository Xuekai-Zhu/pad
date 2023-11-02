def solution():
    # Calculate the total cost of 18 hours of piano lessons
    cost_per_lesson = 30
    length_of_lesson = 1.5  # hours
    total_lessons = 18 / length_of_lesson
    total_cost = total_lessons * cost_per_lesson
    result = total_cost
    return result

print(solution())