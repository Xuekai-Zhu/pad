def solution():
    """There are 30 different nuts in a bowl. If 5/6 of the nuts were eaten, how many nuts were left?"""
    total_nuts = 30
    eaten_nuts = total_nuts * (5/6)
    remaining_nuts = total_nuts - eaten_nuts
    result = remaining_nuts
    return result

print(solution())