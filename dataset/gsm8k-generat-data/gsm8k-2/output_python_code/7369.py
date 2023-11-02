def solution():
    """Jame gets 20 singing lessons. He gets the first lesson free and after the first 10 paid lessons he only needs to pay for every other lesson. Each lesson is $5. His uncle pays for half. How much does James pay?"""
    total_lessons = 20
    free_lessons = 1
    paid_lessons = total_lessons - free_lessons
    every_other_price = 5
    regular_price = every_other_price * 2
    first_10_price = regular_price * 10
    remaining_lessons = paid_lessons - 10
    remaining_price = remaining_lessons * every_other_price
    total_price = first_10_price + remaining_price
    uncle_pays = total_price / 2
    james_pays = total_price - uncle_pays
    result = james_pays
    return result

print(solution())