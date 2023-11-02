def solution():
    
    total_judges = 40
    under_30 = int(total_judges * 0.1)
    from_30_to_50 = int(total_judges * 0.6)
    over_50 = total_judges - under_30 - from_30_to_50
    result = over_50
    return result

print(solution())