def solution():
    """Aaron has four times as many cows as does Matthews. Together, they have 30 more cows than Marovich. If Matthews has 60 cows, how many cows do the three have altogether?"""
    matthews_cows = 60
    aaron_cows = 4 * matthews_cows
    marovich_cows = aaron_cows + matthews_cows - 30
    total_cows = aaron_cows + matthews_cows + marovich_cows
    result = total_cows
    return result

print(solution())