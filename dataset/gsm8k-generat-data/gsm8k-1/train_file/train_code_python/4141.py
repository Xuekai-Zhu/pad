def solution():
    """Quinten sees three buildings downtown and decides to estimate their heights. He knows from a book on local buildings that the one in the middle is 100 feet tall. The one on the left looks like it is 80% of the height of the middle one. The one on the right looks 20 feet shorter than if the building on the left and middle were stacked on top of each other. How tall does Quinten estimate their total height to be?"""
    middle_building = 100
    left_building = middle_building * 0.8
    right_building = (middle_building + left_building) - 20
    total_height = middle_building + left_building + right_building
    result = total_height
    return result

print(solution())