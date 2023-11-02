def solution():
    """Jame gets 20 singing lessons. He gets the first lesson free and after the first 10 paid lessons he only needs to pay for every other lesson. Each lesson is $5. His uncle pays for half. How much does James pay?"""
    total_lessons = 20
    free_lessons = 1
    paid_lessons = total_lessons - free_lessons
    first_10_cost = 10 * 5
    remaining_lessons = paid_lessons - 10 // 2
    remaining_cost = remaining_lessons * 5
    total_cost = first_10_cost + remaining_cost
    uncle_contribution = total_cost / 2
    james_payment = total_cost - uncle_contribution
    result = james_payment
    return result

print(solution())