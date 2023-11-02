def solution():
    # Calculate the total number of bottles that will be placed in the crates
    bottles_in_crates = 12 * 10  # Joshua packs 12 bottles in each crate and has 10 crates
    # Calculate the number of bottles that will not be placed in a crate
    bottles_not_in_crates = 130 - bottles_in_crates
    result = bottles_not_in_crates
    return result

print(solution())