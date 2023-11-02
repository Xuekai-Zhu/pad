def solution():
    piano_cost = 500
    num_lessons = 20
    lesson_cost = 40
    discount = 0.25  # 25% discount

    # Calculate the total cost of piano and lessons without discount
    total_cost_before_discount = piano_cost + (num_lessons * lesson_cost)

    # Calculate the total cost of lessons with discount
    total_lesson_cost_after_discount = (lesson_cost * num_lessons) * (1 - discount)

    # Calculate the total cost of everything
    total_cost = piano_cost + total_lesson_cost_after_discount
    result = total_cost
    return result

print(solution())