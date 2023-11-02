def solution():
    cans_per_carton = 20  # Each carton contains 20 cans of juice
    total_cartons = 50  # 50 cartons have been packed
    loaded_cartons = 40  # 40 cartons have been loaded on a truck

    # Calculate the number of cans already loaded on the truck
    loaded_cans = loaded_cartons * cans_per_carton

    # Calculate the number of cans left to be loaded on the truck
    remaining_cans = (total_cartons - loaded_cartons) * cans_per_carton
    result = remaining_cans
    return result

print(solution())