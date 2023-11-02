def solution():
    white_fish_ratio = 5
    black_fish_ratio = 10
    multicolor_fish_ratio = 12

    num_white_ducks = 3
    num_black_ducks = 7
    num_multicolor_ducks = 6

    # Calculate the total number of fish contributed by the white ducks
    total_white_fish = num_white_ducks * white_fish_ratio

    # Calculate the total number of fish contributed by the black ducks
    total_black_fish = num_black_ducks * black_fish_ratio

    # Calculate the total number of fish contributed by the multicolor ducks
    total_multicolor_fish = num_multicolor_ducks * multicolor_fish_ratio

    # Calculate the total number of fish in the lake
    total_fish = total_white_fish + total_black_fish + total_multicolor_fish
    result = total_fish
    return result

print(solution())