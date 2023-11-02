def solution():
    initial_amount = 200
    fraction_spent = 4/5

    amount_spent = initial_amount * fraction_spent
    amount_left = initial_amount - amount_spent

    result = amount_left
    return result

print(solution())