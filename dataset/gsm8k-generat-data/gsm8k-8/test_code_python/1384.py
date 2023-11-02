def solution():
    # Calculate the number of pots that can be stacked on each shelf
    pots_per_shelf = 5 * 3

    # Calculate the number of shelves needed to stack all the pots
    shelves_needed = 60 / pots_per_shelf

    # Round up to the nearest integer to account for partial shelves
    shelves_needed = math.ceil(shelves_needed)

    result = shelves_needed
    return result

print(solution())