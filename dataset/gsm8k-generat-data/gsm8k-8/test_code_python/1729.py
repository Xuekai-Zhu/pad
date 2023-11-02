def solution():
    # Define the number of giant roaches, scorpions, and crickets
    giant_roaches = 12
    scorpions = 3
    crickets = giant_roaches / 2

    # Define the number of caterpillars
    caterpillars = 2 * scorpions

    # Calculate the total number of insects
    total_insects = giant_roaches + scorpions + crickets + caterpillars
    result = total_insects
    return result

print(solution())