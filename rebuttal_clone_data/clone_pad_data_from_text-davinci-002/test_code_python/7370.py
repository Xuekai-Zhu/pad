def solution():
    total_lessons = 20
    free_lessons = 1
    paid_lessons = total_lessons - free_lessons
    every_other_paid_lesson = paid_lessons / 2
    total_paid_lessons = paid_lessons + every_other_paid_lesson
    lesson_cost = 5
    total_cost = total_paid_lessons * lesson_cost
    uncle_payment = total_cost / 2
    james_payment = total_cost - uncle_payment
    result = james_payment
    
    return result

print(solution())