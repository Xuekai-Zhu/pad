def solution():
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