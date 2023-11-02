def solution():
     watermelon_seeds_yeon = 3 * watermelon_seeds_gwi
     watermelon_seeds_gwi = watermelon_seeds_bom + 40
     watermelon_seeds_bom = 300
     total_seeds = watermelon_seeds_yeon + watermelon_seeds_gwi + watermelon_seeds_bom
     result = total_seeds
     return result

print(solution())