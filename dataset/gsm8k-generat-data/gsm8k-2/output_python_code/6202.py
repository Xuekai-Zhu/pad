def solution():
    """A set of 7 spoons costs $21. If each spoon would be sold separately, how much would 5 spoons cost?"""
    set_price = 21
    set_size = 7
    spoon_price = set_price / set_size
    five_spoons_price = spoon_price * 5
    result = five_spoons_price
    return result

print(solution())