def solution():
    """Bill and Ted went into the forest to gather some wild mushrooms. Bill gathered 12 red mushrooms and 6 brown mushrooms.  Ted gathered 14 green mushrooms and 6 blue mushrooms.  If half of the blue mushrooms, two-thirds of the red mushrooms, and all of the brown mushrooms have white spots, how many white-spotted mushrooms did they gather?"""
    # Calculate the number of white-spotted red mushrooms
    white_red = 2/3 * 12

    # Calculate the number of white-spotted brown mushrooms
    white_brown = 6

    # Calculate the number of white-spotted blue mushrooms
    white_blue = 1/2 * 6

    # Calculate the total number of white-spotted mushrooms
    total_white = white_red + white_brown + white_blue

    # Display the total number of white-spotted mushrooms
    result = total_white
    return result

print(solution())