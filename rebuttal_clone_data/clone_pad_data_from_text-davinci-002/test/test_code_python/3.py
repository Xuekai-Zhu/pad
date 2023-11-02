def solution():
    
    initial_weight = 2
    weight_after_jelly_beans = initial_weight * 3
    weight_after_brownies = weight_after_jelly_beans + 2
    weight_after_gummy_worms = weight_after_brownies * 2
    final_weight = weight_after_gummy_worms
    return final_weight

print(solution())