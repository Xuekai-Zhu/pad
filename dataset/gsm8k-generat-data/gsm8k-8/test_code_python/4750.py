def solution():
    # Calculate the number of fish in Onum Lake
    onum_trout = 75 + 25
    onum_total_fish = onum_trout

    # Calculate the number of fish in Riddle Pond
    riddle_total_fish = onum_total_fish / 2

    # Calculate the total number of fish
    total_fish = 75 + onum_total_fish + riddle_total_fish

    # Calculate the average number of fish
    average_fish = total_fish / 3

    result = average_fish
    return result

print(solution())