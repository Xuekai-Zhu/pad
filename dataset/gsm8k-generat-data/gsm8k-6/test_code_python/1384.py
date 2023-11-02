def solution():
    # Calculate the number of pots that can be stacked on each shelf
    pots_per_shelf = 5 * 3  # 5 pots vertically and 3 sets side-by-side

    # Calculate the number of shelves needed to stock all the pots
    shelves_needed = 60 // pots_per_shelf  # integer division to avoid partial shelves
    if 60 % pots_per_shelf != 0:  # if there are any remaining pots
        shelves_needed += 1  # add one more shelf

    result = shelves_needed
    return result

print(solution())