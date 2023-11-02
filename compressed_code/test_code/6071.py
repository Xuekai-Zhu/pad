def solution():
    
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