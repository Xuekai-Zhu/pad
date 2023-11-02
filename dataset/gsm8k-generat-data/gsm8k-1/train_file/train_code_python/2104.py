def solution():
    """Tom decides to take 10 dance lessons that cost $10 each, but he gets two of them for free. How much does he pay?"""
    lesson_cost = 10
    total_lessons = 10
    free_lessons = 2
    total_cost = (total_lessons - free_lessons) * lesson_cost
    result = total_cost
    return result

print(solution())