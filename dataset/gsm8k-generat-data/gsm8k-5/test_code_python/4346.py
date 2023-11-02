def solution():
    num_orange_julio = 4
    num_grape_julio = 7
    num_orange_mateo = 1
    num_grape_mateo = 3
    liters_per_bottle = 2

    # Calculate total liters of orange and grape soda for Julio and Mateo
    total_liters_julio = (num_orange_julio + num_grape_julio) * liters_per_bottle
    total_liters_mateo = (num_orange_mateo + num_grape_mateo) * liters_per_bottle

    # Calculate the difference in total liters of soda
    difference = total_liters_julio - total_liters_mateo
    result = difference
    return result

print(solution())