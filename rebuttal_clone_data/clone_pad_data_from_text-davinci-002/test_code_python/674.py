def solution():
    level_one_spots = 58
    level_two_spots = level_one_spots + 2
    level_three_spots = level_two_spots + 5
    level_four_spots = level_three_spots + 31
    total_spots = level_one_spots + level_two_spots + level_three_spots + level_four_spots
    result = total_spots
    
    return result

print(solution())