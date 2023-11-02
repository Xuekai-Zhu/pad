def solution():
    num_candy_canes_per_cavity = 4
    num_cavities = 0

    # Calculate the number of candy canes Andy gets from his parents
    num_candy_canes = 2
    num_cavities += num_candy_canes // num_candy_canes_per_cavity

    # Calculate the number of candy canes Andy gets from his teachers
    num_candy_canes = 3 * 4
    num_cavities += num_candy_canes // num_candy_canes_per_cavity

    # Calculate the number of candy canes Andy buys with his allowance
    num_candy_canes = (2 + 3 * 4) * (1 / 7)
    num_cavities += num_candy_canes // num_candy_canes_per_cavity

    result = num_cavities
    return result

print(solution())