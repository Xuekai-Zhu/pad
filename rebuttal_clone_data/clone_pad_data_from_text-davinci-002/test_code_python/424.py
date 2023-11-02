def solution():
    initial_amount = 10000
    amount_cooked_1 = initial_amount * 9/10
    amount_left = initial_amount - amount_cooked_1
    amount_cooked_2 = amount_left * 1/4
    amount_left = amount_left - amount_cooked_2
    result = amount_left
    return result

print(solution())