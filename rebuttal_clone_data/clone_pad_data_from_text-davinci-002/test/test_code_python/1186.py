def solution():
    cost_per_lesson = 10
    free_lessons = 2
    total_lessons = 10
    paid_lessons = total_lessons - free_lessons
    total_cost = cost_per_lesson * paid_lessons
    result = total_cost
    return result

print(solution())