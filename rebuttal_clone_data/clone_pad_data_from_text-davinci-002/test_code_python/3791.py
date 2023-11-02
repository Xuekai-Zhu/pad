def solution():
    initial_amount = 600
    amount_spent_on_clothes = initial_amount / 2
    amount_spent_on_books = amount_spent_on_clothes / 2
    final_amount = initial_amount - amount_spent_on_clothes - amount_spent_on_books
    result = final_amount
    return result

print(solution())