def solution():
    
    total_dollars = 100
    jeff_ratio = 4
    brad_dollars = total_dollars / (jeff_ratio + brad_ratio)
    jeff_dollars = jeff_ratio * brad_dollars
    result = jeff_dollars
    return result

print(solution())