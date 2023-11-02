def solution():
    
    blue_eggs_ratio = 4/5
    blue_eggs_5_candy_ratio = 1/4
    purple_eggs_ratio = 1/5
    purple_eggs_5_candy_ratio = 1/2
    total_blue_eggs = blue_eggs_ratio * 100
    total_purple_eggs = purple_eggs_ratio * 100
    total_blue_eggs_5_candy = total_blue_eggs * blue_eggs_5_candy_ratio
    total_purple_eggs_5_candy = total_purple_eggs * purple_eggs_5_candy_ratio
    total_eggs_5_candy = total_blue_eggs_5_candy + total_purple_eggs_5_candy
    total_eggs_1_candy = 100 - total_eggs_5_candy
    chance_of_5_candy = (total_eggs_5_candy / 100) * 100
    result = chance_of_5_candy
    return result

print(solution())