def solution():
    """Sam has 18 cows. 5 more than half the cows are black. How many cows are not black?"""
    total_cows = 18
    black_cows = (total_cows // 2) + 5
    non_black_cows = total_cows - black_cows
    result = non_black_cows
    return result

print(solution())