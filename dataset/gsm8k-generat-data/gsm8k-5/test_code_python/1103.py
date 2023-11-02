def solution():
    centerpieces = 6  # Martha is making 6 centerpieces
    roses_per_centerpiece = 8  # Each centerpiece uses 8 roses
    orchids_per_centerpiece = 2 * roses_per_centerpiece  # Each centerpiece uses twice as many orchids as roses

    # Calculate the total number of flowers used in all the centerpieces
    total_flowers = (roses_per_centerpiece + orchids_per_centerpiece) * centerpieces

    # Calculate the total cost of the flowers used in all the centerpieces
    total_cost = total_flowers * 15

    # Calculate the number of lilies used in each centerpiece
    lilies_per_centerpiece = (2700 - total_cost) / (centerpieces * 15)

    result = lilies_per_centerpiece
    return result

print(solution())