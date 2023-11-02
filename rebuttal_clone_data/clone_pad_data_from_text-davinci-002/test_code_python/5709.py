def solution():
    cloves_per_vampire = 3/2
    cloves_per_wight = 3
    cloves_per_vampire_bat = 8/3
    total_cloves = (30 * cloves_per_vampire) + (12 * cloves_per_wight) + (40 * cloves_per_vampire_bat)
    result = total_cloves
    return result

print(solution())