def solution():
    # Define the number of fish Micah has
    micah_fish = 7

    # Define the number of fish Kenneth has
    kenneth_fish = 3 * micah_fish

    # Define the number of fish Matthias has
    matthias_fish = kenneth_fish - 15

    # Calculate the total number of fish
    total_fish = micah_fish + kenneth_fish + matthias_fish
    result = total_fish
    return result

print(solution())