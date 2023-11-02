def solution():
    micah_fish = 7  # Micah has 7 fish
    kenneth_fish = 3 * micah_fish  # Kenneth has three times as many fish as Micah
    matthias_fish = kenneth_fish - 15  # Matthias has 15 less fish than Kenneth
    total_fish = micah_fish + kenneth_fish + matthias_fish  # Total number of fish

    result = total_fish
    return result

print(solution())