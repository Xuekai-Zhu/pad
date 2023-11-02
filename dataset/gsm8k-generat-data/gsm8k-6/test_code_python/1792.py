def solution():
    # Calculate the total number of flowers required for one centerpiece
    roses = 8
    daisies = 12
    snapdragons = 3
    lilies = 2 * snapdragons
    total_flowers = roses + daisies + snapdragons + lilies

    # Calculate the total number of flowers required for all centerpieces
    centerpieces = 10
    total_flowers *= centerpieces
    result = total_flowers
    return result

print(solution())