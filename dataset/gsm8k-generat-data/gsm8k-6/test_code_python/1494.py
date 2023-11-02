def solution():
    # Calculate the number of fish each boy has
    micah_fish = 7
    kenneth_fish = 3 * micah_fish
    matthias_fish = kenneth_fish - 15

    # Calculate the total number of fish
    total_fish = micah_fish + kenneth_fish + matthias_fish
    result = total_fish
    return result

print(solution())