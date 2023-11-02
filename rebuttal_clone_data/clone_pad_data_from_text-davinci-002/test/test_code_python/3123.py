def solution():
    cattle = 555
    cows = 10
    bulls = 27
    total_cattle = cows + bulls
    cattle_ratio = cattle / total_cattle
    bull_ratio = bulls / total_cattle
    cattle_amount = cattle_ratio * cattle
    bull_amount = bull_ratio * cattle
    result = bull_amount
    return result

print(solution())