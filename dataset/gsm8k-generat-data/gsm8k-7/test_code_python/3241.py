def solution():
    fish_per_roll = 40
    total_fish = 400
    bad_fish_ratio = 0.2

    # Calculate the number of fish that were not bad
    good_fish = total_fish * (1 - bad_fish_ratio)

    # Calculate the number of sushi rolls that can be made with the good fish
    num_rolls = good_fish // fish_per_roll

    result = num_rolls
    return result

print(solution())