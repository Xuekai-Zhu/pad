def solution():
    cans_per_carton = 20
    total_cartons = 50
    loaded_cartons = 40

    # Calculate the total number of cans packed
    total_cans_packed = cans_per_carton * total_cartons

    # Calculate the number of cans already loaded
    loaded_cans = cans_per_carton * loaded_cartons

    # Calculate the number of cans left to be loaded
    cans_left = total_cans_packed - loaded_cans
    result = cans_left
    return result

print(solution())