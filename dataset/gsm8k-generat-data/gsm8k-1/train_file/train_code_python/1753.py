def solution():
    """Emma got $2000 from the bank. She bought $400 of furniture and gave 3/4 of the rest to her friend Anna. How much is left with Emma?"""
    initial_amount = 2000
    furniture_cost = 400
    remaining_amount = initial_amount - furniture_cost
    amount_given = remaining_amount * 3/4
    amount_left = remaining_amount - amount_given
    result = amount_left
    return result

print(solution())