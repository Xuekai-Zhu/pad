def solution():
    """Jame gets 20 singing lessons. He gets the first lesson free and after the first 10 paid lessons he only needs to pay for every other lesson. Each lesson is $5. His uncle pays for half. How much does James pay?"""
    # Define the price per lesson and the number of free lessons
    PRICE_PER_LESSON = 5
    FREE_LESSONS = 1

    # Calculate the number of paid lessons and the number of lessons James needs to pay for
    paid_lessons = 20 - FREE_LESSONS
    paid_lessons_after_ten = paid_lessons - 10
    paid_lessons_every_other = (paid_lessons_after_ten // 2) + 10

    # Calculate the total cost of the lessons and the amount James' uncle pays
    total_cost = PRICE_PER_LESSON * paid_lessons_every_other
    uncle_payment = total_cost / 2

    # Calculate the amount James pays
    james_payment = total_cost - uncle_payment

    # Return the result
    result = james_payment
    return result

print(solution())