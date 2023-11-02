def solution():
    
    piano_cost = 500
    lesson_cost = 40
    num_lessons = 20
    discount = 0.25

    lesson_cost_after_discount = lesson_cost - lesson_cost * discount
    total_lesson_cost = lesson_cost_after_discount * num_lessons
    total_cost = piano_cost + total_lesson_cost
    result = total_cost
    return result

print(solution())