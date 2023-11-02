def solution():
    num_lessons = 10
    lesson_cost = 10.0

    # Calculate the total cost of all 10 lessons
    total_cost = num_lessons * lesson_cost

    # Calculate the cost of the two free lessons
    free_lessons_cost = lesson_cost * 2

    # Subtract the cost of the two free lessons from the total cost
    total_cost -= free_lessons_cost
    result = total_cost
    return result

print(solution())