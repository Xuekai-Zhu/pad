def solution():
    # Define the number of forks and knives
    forks = 6
    knives = forks + 9

    # Define the number of spoons and teaspoons
    spoons = 2 * knives
    teaspoons = forks / 2

    # Add 2 of each cutlery to the drawer
    forks += 2
    knives += 2
    spoons += 2
    teaspoons += 2

    # Calculate the total number of pieces of cutlery
    total_cutlery = forks + knives + spoons + teaspoons
    result = total_cutlery
    return result

print(solution())