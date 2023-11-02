def solution():
    # Define the number of fish needed for one sushi roll
    fish_per_roll = 40

    # Define the total number of fish bought
    total_fish = 400

    # Calculate the number of fish that have gone bad
    bad_fish = total_fish * 0.2

    # Calculate the number of usable fish
    usable_fish = total_fish - bad_fish

    # Calculate the number of sushi rolls that can be made
    sushi_rolls = usable_fish // fish_per_roll

    result = sushi_rolls
    return result

print(solution())