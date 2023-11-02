def solution():
    middle_building_height = 100  # The middle building is 100 feet tall
    left_building_height = 0.8 * middle_building_height  # The left building is 80% of the middle building's height
    right_building_height = (middle_building_height + left_building_height) - 20  # The right building is 20 feet shorter than if the left and middle buildings were stacked

    # Calculate the total estimated height of the three buildings
    total_height = middle_building_height + left_building_height + right_building_height
    result = total_height
    return result

print(solution())