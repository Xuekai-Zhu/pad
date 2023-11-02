def solution():
    piano_cost = 500  # John spends $500 on a piano
    num_lessons = 20  # John takes 20 lessons
    lesson_cost = 40  # John pays $40 per lesson
    discount = 0.25  # John gets a 25% discount on the lesson cost

    # Calculate the total cost of the lessons before the discount
    total_lesson_cost = num_lessons * lesson_cost

    # Calculate the total cost of the lessons after the discount
    discounted_lesson_cost = total_lesson_cost * (1 - discount)

    # Calculate the total cost of everything
    total_cost = piano_cost + discounted_lesson_cost
    result = total_cost
    return result

print(solution())