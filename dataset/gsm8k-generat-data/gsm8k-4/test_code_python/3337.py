def solution():
    """Bill and Ted went into the forest to gather some wild mushrooms. Bill gathered 12 red mushrooms and 6 brown mushrooms. Ted gathered 14 green mushrooms and 6 blue mushrooms. If half of the blue mushrooms, two-thirds of the red mushrooms, and all of the brown mushrooms have white spots, how many white-spotted mushrooms did they gather?"""
    # Define the number of mushrooms gathered by each person
    bill_red = 12
    bill_brown = 6
    ted_green = 14
    ted_blue = 6

    # Calculate the number of white-spotted mushrooms gathered
    white_spotted = (bill_brown + (2/3)*bill_red + (1/2)*ted_blue)

    # Return the result
    result = white_spotted
    return result

print(solution())