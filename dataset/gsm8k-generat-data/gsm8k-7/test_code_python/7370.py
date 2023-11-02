def solution():
    num_lessons = 20
    free_lessons = 1
    paid_lessons = 10
    alternate_lessons = 5
    lesson_cost = 5
    uncle_payment = 0.5

    # Calculate the total cost of the first 10 paid lessons
    total_paid_lessons = (paid_lessons - free_lessons) / 2 * lesson_cost

    # Calculate the total cost of the remaining 10 lessons
    total_remaining_lessons = (num_lessons - paid_lessons) / alternate_lessons * lesson_cost

    # Calculate James' total cost
    total_cost = total_paid_lessons + total_remaining_lessons

    # Calculate the amount James' uncle pays
    uncle_paid = total_cost * uncle_payment

    # Calculate the amount James pays
    james_paid = total_cost - uncle_paid

    result = james_paid
    return result

print(solution())