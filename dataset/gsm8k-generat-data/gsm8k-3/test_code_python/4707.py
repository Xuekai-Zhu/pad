def solution():
    """For every white duck at the lake there are 5 fish.  For every black duck there are 10 fish and for every multicolor duck there are 12 fish.  Currently there are 3 white ducks, 7 black ducks and 6 multicolored ducks.  How many fish are in the lake?"""
    # Define the fish-to-duck ratios
    WHITE_DUCK_RATIO = 5
    BLACK_DUCK_RATIO = 10
    MULTICOLOR_DUCK_RATIO = 12

    # Define the number of each type of duck
    white_ducks = 3
    black_ducks = 7
    multicolor_ducks = 6

    # Calculate the total number of fish
    total_fish = (white_ducks * WHITE_DUCK_RATIO) + (black_ducks * BLACK_DUCK_RATIO) + (multicolor_ducks * MULTICOLOR_DUCK_RATIO)

    # Display the total number of fish
    result = total_fish
    return result

print(solution())