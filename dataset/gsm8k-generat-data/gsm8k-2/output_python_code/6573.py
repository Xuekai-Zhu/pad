def solution():
    """Jack borrowed $1200 from Jill, which he promised to pay back with an interest of 10%. How much will Jack pay back?"""
    borrowed_amount = 1200
    interest_rate = 0.1
    interest_amount = borrowed_amount * interest_rate
    total_amount = borrowed_amount + interest_amount
    result = total_amount
    return result

print(solution())