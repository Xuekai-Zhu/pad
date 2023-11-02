def solution():
    # Calculate the total catch before the accident
    jordan_catch = 4
    perry_catch = jordan_catch * 2
    total_catch = jordan_catch + perry_catch

    # Calculate the number of fish lost in the accident
    lost_fish = total_catch / 4

    # Calculate the number of fish remaining
    remaining_fish = total_catch - lost_fish
    result = remaining_fish
    return result

print(solution())