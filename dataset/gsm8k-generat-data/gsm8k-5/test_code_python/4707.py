def solution():
    white_ducks = 3
    black_ducks = 7
    multicolor_ducks = 6

    # Calculate the number of fish for each duck type
    white_fish = 5 * white_ducks
    black_fish = 10 * black_ducks
    multicolor_fish = 12 * multicolor_ducks

    # Calculate the total number of fish in the lake
    total_fish = white_fish + black_fish + multicolor_fish
    result = total_fish
    return result

print(solution())