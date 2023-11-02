def solution():
    height_first_week = 2  # The corn plants grew 2 inches in the first week
    height_second_week = 2 * 2  # The corn plants grew twice as much as the first week in the second week
    height_third_week = 4 * height_second_week  # The corn plants grew 4 times as much as the second week in the third week
    
    total_height = height_first_week + height_second_week + height_third_week  # Calculate the total height of the corn plants
    
    result = total_height
    return result

print(solution())