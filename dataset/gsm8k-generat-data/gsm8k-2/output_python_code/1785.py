def solution():
    """4/5 of the Easter eggs are blue and 1/5 are purple. Half the purple eggs have five pieces of candy each, and 1/4 of the blue eggs do. The rest of the eggs only have one piece of candy. If Jerry opens one egg at random, what is the percentage chance he'll get 5 pieces of candy?"""
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