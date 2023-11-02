def solution():
    
    blonde_hair_dolls = 4
    brown_hair_dolls = 4 * blonde_hair_dolls
    black_hair_dolls = brown_hair_dolls - 2
    total_non_blonde = brown_hair_dolls + black_hair_dolls
    difference = total_non_blonde - blonde_hair_dolls
    result = difference
    return result

print(solution())