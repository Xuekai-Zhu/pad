def solution():
    
    num_cakes = 2
    egg_whites_per_cake = 8
    tablespoons_per_egg_white = 2
    total_egg_whites = num_cakes * egg_whites_per_cake
    total_aquafaba = total_egg_whites * tablespoons_per_egg_white
    result = total_aquafaba
    return result

print(solution())