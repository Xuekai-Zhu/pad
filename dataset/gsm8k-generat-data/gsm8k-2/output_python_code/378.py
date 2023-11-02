def solution():
    """John decides to learn how to play the piano. He buys a piano for $500. He then hires a teacher for 20 lessons at $40 per lesson but ends up getting a 25% discount. How much did everything cost?"""
    piano_cost = 500
    lesson_cost = 40
    num_lessons = 20
    discount = 0.25

    lesson_cost_after_discount = lesson_cost - lesson_cost * discount
    total_lesson_cost = lesson_cost_after_discount * num_lessons
    total_cost = piano_cost + total_lesson_cost
    result = total_cost
    return result

print(solution())