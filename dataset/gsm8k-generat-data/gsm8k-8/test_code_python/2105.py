def solution():
    # Define the cost and number of lessons
    cost_per_lesson = 10
    num_lessons = 10
    num_free_lessons = 2

    # Calculate the total cost
    total_cost = (num_lessons - num_free_lessons) * cost_per_lesson
    result = total_cost
    return result

print(solution())