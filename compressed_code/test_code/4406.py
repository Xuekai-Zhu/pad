def solution():
    
    cloves_per_vampire = 3/2
    cloves_per_bat = 3/8
    cloves_per_wight = 1
    total_cloves = cloves_per_vampire * 30 + cloves_per_wight * 12 + cloves_per_bat * 40
    result = total_cloves
    return result

print(solution())