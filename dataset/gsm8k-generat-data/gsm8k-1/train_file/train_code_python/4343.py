def solution():
    """Allie has 9 toys, which are in total worth $52. If we know that one toy is worth $12, and all the other toys have the same value, how much does one of the other toys cost?"""
    total_toys = 9
    total_worth = 52
    one_toy_worth = 12
    other_toy_worth = (total_worth - one_toy_worth) / (total_toys - 1)
    result = other_toy_worth
    return result

print(solution())