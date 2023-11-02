def solution():
    apple_pies_baked = 3 * 12
    cherry_pies_baked = 2 * 12
    pies_baked_per_week = apple_pies_baked + cherry_pies_baked
    difference = apple_pies_baked - cherry_pies_baked
    return pies_baked_per_week, difference

print(solution())