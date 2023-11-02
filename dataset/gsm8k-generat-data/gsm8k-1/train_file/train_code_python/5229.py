def solution():
    """Tara's parents gave her $90 for her birthday. Not wanting to spend it, Tara put the money in a new bank account that gains 10% interest annually. If she doesn't withdraw the money at all, how much will she have after a year?"""
    initial_amount = 90
    annual_interest_rate = 0.1
    final_amount = initial_amount + (initial_amount * annual_interest_rate)
    result = final_amount
    return result

print(solution())