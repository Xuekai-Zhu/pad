def solution():
    """Micheal decided to take some piano lessons. One lesson costs $30 and lasts for 1.5 hours. How much will Micheal need to pay for 18 hours of lessons?"""
    lesson_cost = 30
    lesson_duration = 1.5
    total_lessons = 18 / lesson_duration
    total_cost = total_lessons * lesson_cost
    result = total_cost
    return result

print(solution())