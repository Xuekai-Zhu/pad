def solution():
    # Calculate the total amount earned by the teacher in 5 weeks
    total_lessons = 5  # Caprice takes one lesson per week for 5 weeks
    lesson_time = 1  # the lesson lasts 1 hour
    lesson_cost = 2 * 10  # the teacher charges $10 for every half hour of teaching
    total_cost = total_lessons * lesson_time * lesson_cost
    result = total_cost
    return result

print(solution())