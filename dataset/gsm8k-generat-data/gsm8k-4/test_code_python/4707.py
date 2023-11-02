def solution():
    """For every white duck at the lake there are 5 fish. For every black duck there are 10 fish and for every multicolor duck there are 12 fish. Currently there are 3 white ducks, 7 black ducks and 6 multicolored ducks. How many fish are in the lake?"""
    # Define the number of white, black and multicolored ducks
    white_ducks = 3
    black_ducks = 7
    multicolor_ducks = 6

    # Calculate the number of fish for each type of duck
    white_fish = white_ducks * 5
    black_fish = black_ducks * 10
    multicolor_fish = multicolor_ducks * 12

    # Calculate the total number of fish
    total_fish = white_fish + black_fish + multicolor_fish

    # return the result
    result = total_fish
    return result

print(solution())