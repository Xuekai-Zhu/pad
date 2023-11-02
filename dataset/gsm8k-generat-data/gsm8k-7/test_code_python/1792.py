def solution():
    roses_per_arrangement = 8
    daisies_per_arrangement = 12
    snapdragons_per_arrangement = 3
    lilies_per_arrangement = 2 * snapdragons_per_arrangement
    arrangements_per_table = 1
    tables = 10

    # Calculate the total number of roses needed for all arrangements
    total_roses = roses_per_arrangement * arrangements_per_table * tables

    # Calculate the total number of daisies needed for all arrangements
    total_daisies = daisies_per_arrangement * arrangements_per_table * tables

    # Calculate the total number of snapdragons needed for all arrangements
    total_snapdragons = snapdragons_per_arrangement * arrangements_per_table * tables

    # Calculate the total number of lilies needed for all arrangements
    total_lilies = lilies_per_arrangement * arrangements_per_table * tables

    # Calculate the total number of flowers needed for all arrangements
    total_flowers = total_roses + total_daisies + total_snapdragons + total_lilies
    result = total_flowers
    return result

print(solution())