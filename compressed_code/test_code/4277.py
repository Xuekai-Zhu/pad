def solution():
    
    total_cattle = 555
    cow_ratio = 10
    bull_ratio = 27
    total_ratio = cow_ratio + bull_ratio
    bull_count = (bull_ratio / total_ratio) * total_cattle
    result = bull_count
    return result

print(solution())