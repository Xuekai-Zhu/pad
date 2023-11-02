def solution():
    
    first_level_spots = 4
    second_level_spots = first_level_spots + 7
    third_level_spots = second_level_spots + 6
    fourth_level_spots = 14
    total_spots = first_level_spots + second_level_spots + third_level_spots + fourth_level_spots
    result = total_spots
    return result

print(solution())