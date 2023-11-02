def solution():
    """Quinten sees three buildings downtown and decides to estimate their heights. He knows from a book on local buildings that the one in the middle is 100 feet tall. The one on the left looks like it is 80% of the height of the middle one. The one on the right looks 20 feet shorter than if the building on the left and middle were stacked on top of each other. How tall does Quinten estimate their total height to be?"""
    middle_building_height = 100
    left_building_height = 0.8 * middle_building_height
    right_building_height = (left_building_height + middle_building_height) - 20
    total_height = left_building_height + middle_building_height + right_building_height
    result = total_height
    return result

print(solution())