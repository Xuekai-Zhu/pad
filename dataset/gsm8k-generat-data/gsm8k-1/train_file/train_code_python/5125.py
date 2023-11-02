def solution():
    """Micheal decided to take some piano lessons. One lesson costs $30 and lasts for 1.5 hours. How much will Micheal need to pay for 18 hours of lessons?"""
    hours_per_lesson = 1.5
    cost_per_lesson = 30
    total_hours = 18
    number_of_lessons = total_hours / hours_per_lesson
    total_cost = number_of_lessons * cost_per_lesson
    result = total_cost
    return result

print(solution())