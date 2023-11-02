def solution():
    """Quinten sees three buildings downtown and decides to estimate their heights. He knows from a book on local buildings that the one in the middle is 100 feet tall. The one on the left looks like it is 80% of the height of the middle one. The one on the right looks 20 feet shorter than if the building on the left and middle were stacked on top of each other. How tall does Quinten estimate their total height to be?"""
    # Define the height of the middle building
    middle_height = 100

    # Calculate the height of the left building
    left_height = middle_height * 0.8

    # Calculate the estimated height of the left and middle buildings stacked on top of each other
    stacked_height = middle_height + left_height

    # Calculate the estimated height of all three buildings
    total_height = stacked_height - 20

    # return the result
    result = total_height
    return result

print(solution())