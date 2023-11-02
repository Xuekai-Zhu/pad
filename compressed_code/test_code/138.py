def solution():
    
    total_crayons = 5 * 24
    unused_crayons = ((24 * 5/8) * 2) + ((24 * 2/3) * 2) + (24 * (1 - 2/3))
    used_crayons = total_crayons - unused_crayons
    result = unused_crayons
    return result

print(solution())