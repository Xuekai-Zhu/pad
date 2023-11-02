def solution():
    # Calculate the number of bottles of domestic wine
    domestic_wine = 2400/2

    # Calculate the total number of bottles of wine
    total_wine = 2400 + domestic_wine

    # Calculate the number of wine bottles drunk at the party
    drunk_wine = total_wine/3

    # Calculate the number of wine bottles remaining in the cellar
    remaining_wine = total_wine - drunk_wine
    result = remaining_wine
    return result

print(solution())