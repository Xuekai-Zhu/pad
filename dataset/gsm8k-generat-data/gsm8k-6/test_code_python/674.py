def solution():
    # Calculate the total number of open parking spots
    open_spots_first_level = 58
    open_spots_second_level = open_spots_first_level + 2
    open_spots_third_level = open_spots_second_level + 5
    open_spots_fourth_level = 31

    total_open_spots = open_spots_first_level + open_spots_second_level + open_spots_third_level + open_spots_fourth_level

    # Calculate the total number of full parking spots
    total_parking_spots = 4 * 100  # 4 levels with 100 spots per level
    full_parking_spots = total_parking_spots - total_open_spots
    result = full_parking_spots
    return result

print(solution())