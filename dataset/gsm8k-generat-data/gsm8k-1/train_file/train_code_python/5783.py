def solution():
    """Jay bought a book for $25, a pen for $4, and a ruler for $1. He paid with a fifty-dollar bill. How much change, in dollars, did Jay get?"""
    total_cost = 25 + 4 + 1
    payment = 50
    change = payment - total_cost
    result = change
    return result

print(solution())