def solution():
    # Define the number of flowers needed for one arrangement
    roses_per_arrangement = 8
    daisies_per_arrangement = 12
    snapdragons_per_arrangement = 3
    lilies_per_arrangement = 2 * roses_per_arrangement

    # Calculate the total number of flowers needed for all arrangements
    total_flowers = (roses_per_arrangement + daisies_per_arrangement
                     + snapdragons_per_arrangement + lilies_per_arrangement)
    total_flowers *= 10

    result = total_flowers
    return result

print(solution())