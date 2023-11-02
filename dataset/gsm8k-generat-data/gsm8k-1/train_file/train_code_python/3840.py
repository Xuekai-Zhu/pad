def solution():
    """Laura bought 2 pairs of pants for $54 each and 4 shirts for $33 each. She gave $250 to the cashier. So how much change did she take?"""
    pants_cost = 54
    shirt_cost = 33
    num_pants = 2
    num_shirts = 4
    total_cost = (pants_cost * num_pants) + (shirt_cost * num_shirts)
    payment = 250
    change = payment - total_cost
    result = change
    return result

print(solution())