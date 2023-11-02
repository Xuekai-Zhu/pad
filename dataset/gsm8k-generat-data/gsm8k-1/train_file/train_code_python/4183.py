def solution():
    """There are 28 garden gnomes in a yard. Three-fourths of them have red hats, and the rest have blue hats. Half the garden gnomes have big noses instead of small noses. If six gnomes with blue hats have big noses, how many gnomes with red hats have small noses?"""
    total_gnomes = 28
    red_hats = 0.75 * total_gnomes
    blue_hats = total_gnomes - red_hats
    big_noses = 0.5 * total_gnomes
    small_noses = total_gnomes - big_noses
    blue_big_noses = 6
    red_small_noses = small_noses - blue_big_noses
    red_small_noses_with_red_hats = red_hats - (blue_hats - blue_big_noses)
    
    result = red_small_noses_with_red_hats
    return result

print(solution())