def solution():
    # Calculate the total area of the 3 paintings that are 5 ft by 5 ft
    area_5x5 = 3 * (5 * 5)

    # Calculate the area of the painting that is 10 ft by 8 ft
    area_10x8 = 10 * 8

    # Calculate the remaining area after accounting for the 3 5x5 paintings and the 10x8 painting
    remaining_area = 200 - area_5x5 - area_10x8

    # Calculate the width of the final painting
    final_height = 5
    final_width = remaining_area / final_height
    result = final_width
    return result

print(solution())