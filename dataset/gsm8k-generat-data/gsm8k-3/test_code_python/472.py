def solution():
    """It takes 7 years for an apple tree to bear fruit. If Lydia planted a tree when she was 4 years old and is now 9 years old, how old would she be when she gets to eat an apple from her tree for the first time?"""
    # Define the number of years it takes for the apple tree to bear fruit
    FRUIT_BEARING_YEARS = 7

    # Calculate the number of years from when the tree was planted to when it bears fruit
    years_to_fruit = FRUIT_BEARING_YEARS - (9 - 4)

    # Calculate Lydia's age when the tree bears fruit
    age_at_fruit_bearing = years_to_fruit + 9

    # Display Lydia's age at fruit bearing
    result = age_at_fruit_bearing
    return result

print(solution())