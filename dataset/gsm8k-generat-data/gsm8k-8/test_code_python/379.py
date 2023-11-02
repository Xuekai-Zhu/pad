def solution():
    piano_cost = 500
    num_lessons = 20
    lesson_cost = 40
    discount = 0.25

    # Calculate the total cost of piano and lessons before discount
    total_cost = piano_cost + (num_lessons * lesson_cost)

    # Apply the discount
    total_cost *= (1 - discount)

    result = total_cost
    return result

print(solution())