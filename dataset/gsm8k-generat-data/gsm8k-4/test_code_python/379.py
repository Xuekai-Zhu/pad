def solution():
    """John decides to learn how to play the piano. He buys a piano for $500. He then hires a teacher for 20 lessons at $40 per lesson but ends up getting a 25% discount. How much did everything cost?"""
    # Define the cost of the piano and the number of lessons
    piano_cost = 500
    num_lessons = 20

    # Calculate the cost of the lessons with the discount
    lesson_cost = 40 * (1-0.25)  # 25% discount
    total_lesson_cost = num_lessons * lesson_cost

    # Calculate the total cost of everything
    total_cost = piano_cost + total_lesson_cost

    # return the result
    result = total_cost
    return result

print(solution())