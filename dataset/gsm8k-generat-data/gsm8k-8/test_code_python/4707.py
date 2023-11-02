def solution():
    # Calculate the total number of fish for each type of duck
    white_duck_fish = 3 * 5
    black_duck_fish = 7 * 10
    multicolor_duck_fish = 6 * 12

    # Calculate the total number of fish in the lake
    total_fish = white_duck_fish + black_duck_fish + multicolor_duck_fish
    result = total_fish
    return result

print(solution())