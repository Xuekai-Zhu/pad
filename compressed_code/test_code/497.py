def solution():
    
    spots_per_level = 100
    first_level_open_spots = 58
    second_level_open_spots = first_level_open_spots + 2
    third_level_open_spots = second_level_open_spots + 5
    fourth_level_open_spots = 31
    total_open_spots = first_level_open_spots + second_level_open_spots + third_level_open_spots + fourth_level_open_spots
    total_full_spots = (4 * spots_per_level) - total_open_spots
    result = total_full_spots
    return result

print(solution())