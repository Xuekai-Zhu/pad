def solution():
    """Mr. Doré bought $140 worth of pants, a $43 shirt and a $15 tie. He pays with a $200 bill. How much will the saleswoman give him back?"""
    total_cost = 140 + 43 + 15
    payment = 200
    change = payment - total_cost
    result = change
    return result

print(solution())