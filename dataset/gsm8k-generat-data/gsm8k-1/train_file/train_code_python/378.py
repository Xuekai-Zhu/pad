def solution():
    """John decides to learn how to play the piano. He buys a piano for $500. He then hires a teacher for 20 lessons at $40 per lesson but ends up getting a 25% discount. How much did everything cost?"""
    piano_cost = 500
    lessons = 20
    lesson_cost = 40
    discount_percent = 25
    discounted_price = lesson_cost - (lesson_cost * (discount_percent / 100))
    total_lesson_cost = lessons * discounted_price
    total_cost = piano_cost + total_lesson_cost
    result = total_cost
    return result

print(solution())