def solution():
    """For every white duck at the lake there are 5 fish. For every black duck there are 10 fish and for every multicolor duck there are 12 fish. Currently there are 3 white ducks, 7 black ducks and 6 multicolored ducks. How many fish are in the lake?"""
    white_fish = 3 * 5
    black_fish = 7 * 10
    multicolor_fish = 6 * 12
    total_fish = white_fish + black_fish + multicolor_fish
    result = total_fish
    return result

print(solution())