def solution():
    # Define the size of Joyce's previous property
    prev_prop_size = 2

    # Define the size of Joyce's new property, including the pond
    new_prop_size = prev_prop_size * 10 + 1

    # Calculate the size of Joyce's new property, excluding the pond
    new_veg_land_size = new_prop_size - 1

    # Return the size of Joyce's new property suitable for growing vegetables
    result = new_veg_land_size
    return result

print(solution())