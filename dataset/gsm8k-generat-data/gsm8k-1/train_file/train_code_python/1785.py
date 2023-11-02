def solution():
    """4/5 of the Easter eggs are blue and 1/5 are purple. Half the purple eggs have five pieces of candy each, and 1/4 of the blue eggs do. The rest of the eggs only have one piece of candy. If Jerry opens one egg at random, what is the percentage chance he'll get 5 pieces of candy?"""
    blue_eggs_ratio = 4/5
    purple_eggs_ratio = 1/5
    purple_eggs_with_5_candy = 1/2 * purple_eggs_ratio
    blue_eggs_with_5_candy = 1/4 * blue_eggs_ratio
    total_eggs_with_5_candy = purple_eggs_with_5_candy + blue_eggs_with_5_candy
    total_eggs = blue_eggs_ratio + purple_eggs_ratio
    percentage_chance = total_eggs_with_5_candy / total_eggs * 100
    result = percentage_chance
    return result

print(solution())