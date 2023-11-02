def solution():
    cost_per_lesson = 10  # Each dance lesson costs $10
    num_lessons = 10  # Tom takes 10 dance lessons
    free_lessons = 2  # Tom gets 2 dance lessons for free

    # Calculate the total cost of the dance lessons
    total_cost = (num_lessons - free_lessons) * cost_per_lesson

    result = total_cost
    return result

print(solution())