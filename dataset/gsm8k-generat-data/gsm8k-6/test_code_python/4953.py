def solution():
    # Calculate the total number of cans that have been packed
    total_cans_packed = 50 * 20  # 50 cartons, each with 20 cans

    # Calculate the total number of cans that have been loaded on the truck
    cans_loaded = 40 * 20  # 40 cartons loaded, each with 20 cans

    # Calculate the number of cans left to be loaded
    cans_left = total_cans_packed - cans_loaded
    result = cans_left
    return result

print(solution())