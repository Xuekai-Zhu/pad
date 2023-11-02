def solution():
    # Calculate the total number of fish caught by Jordan and Perry
    jordan_catch = 4
    perry_catch = 2 * jordan_catch
    total_catch = jordan_catch + perry_catch

    # Calculate the number of fish lost after the boat tipped over
    lost_fish = total_catch / 4

    # Calculate the number of fish remaining
    remaining_fish = total_catch - lost_fish
    result = remaining_fish
    return result

print(solution())