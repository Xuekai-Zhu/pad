def solution():
    # Calculate the height of the building on the left
    left_building_height = 0.8 * 100  # 80% of the height of the middle building

    # Calculate the height of the building on the right
    right_building_height = (100 + left_building_height) - 20  # 20 feet shorter than if the left and middle buildings were stacked

    # Calculate the estimated total height of the three buildings
    total_height = left_building_height + 100 + right_building_height

    result = total_height
    return result

print(solution())