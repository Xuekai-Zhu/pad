def solution():
    # Calculate the total number of candy canes Andy receives
    candy_canes_from_parents = 2
    candy_canes_from_teachers = 3 * 4
    total_candy_canes = candy_canes_from_parents + candy_canes_from_teachers

    # Calculate the number of candy canes Andy buys with his allowance
    allowance_candy_canes = total_candy_canes * (1/7)

    # Calculate the total number of candy canes Andy eats
    total_candy_canes_eaten = total_candy_canes + allowance_candy_canes

    # Calculate the total number of cavities Andy gets
    cavities_per_candy_cane = 1/4
    total_cavities = cavities_per_candy_cane * total_candy_canes_eaten

    result = total_cavities
    return result

print(solution())