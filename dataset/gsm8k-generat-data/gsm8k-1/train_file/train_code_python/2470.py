def solution():
    """John books 3 nights at a hotel room for $250 a night. He has a $100 discount. How much does he pay?"""
    nights = 3
    nightly_rate = 250
    discount = 100
    total_cost = nights * nightly_rate - discount
    result = total_cost
    return result

print(solution())