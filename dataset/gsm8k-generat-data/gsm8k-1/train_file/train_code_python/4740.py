def solution():
    """Carson counts 6 clouds that look like funny animals. His little brother counts three times as many clouds that look like dragons. How many clouds did they count in total?"""
    num_funny_animal_clouds = 6
    num_dragon_clouds = 3 * num_funny_animal_clouds
    total_clouds = num_funny_animal_clouds + num_dragon_clouds
    result = total_clouds
    return result

print(solution())