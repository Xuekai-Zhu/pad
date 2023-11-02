def solution():
    """For every white duck at the lake there are 5 fish. For every black duck there are 10 fish and for every multicolor duck there are 12 fish. Currently there are 3 white ducks, 7 black ducks and 6 multicolored ducks. How many fish are in the lake?"""
    white_ducks = 3
    black_ducks = 7
    multicolor_ducks = 6
    fish_per_white_duck = 5
    fish_per_black_duck = 10
    fish_per_multicolor_duck = 12
    total_fish = (white_ducks * fish_per_white_duck) + (black_ducks * fish_per_black_duck) + (multicolor_ducks * fish_per_multicolor_duck)
    result = total_fish
    return result

print(solution())