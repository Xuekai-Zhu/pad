def solution():
    """John decides to learn how to play the piano.  He buys a piano for $500.  He then hires a teacher for 20 lessons at $40 per lesson but ends up getting a 25% discount.  How much did everything cost?"""
    # Calculate the cost of the piano
    piano_cost = 500

    # Calculate the cost of the piano lessons
    lesson_cost_per = 40
    lesson_discount = 0.25
    lesson_count = 20
    lesson_cost = lesson_count * lesson_cost_per * (1 - lesson_discount)

    # Calculate the total cost
    total_cost = piano_cost + lesson_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())