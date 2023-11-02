def solution():
    """Jack and Jill are friends who borrow from each other often. Last week Jack borrowed $1200 from Jill, which he promised to pay back with an interest of 10%. How much will Jack pay back?"""
    borrowed_amount = 1200
    interest_rate = 10
    interest_amount = borrowed_amount * (interest_rate / 100)
    total_amount = borrowed_amount + interest_amount
    result = total_amount
    return result

print(solution())