def solution():
    # Calculate the total number of bottles that will be placed in the crates
    bottles_in_crates = 12 * 10

    # Calculate the number of bottles that will not be placed in a crate
    remaining_bottles = 130 - bottles_in_crates
    result = remaining_bottles
    return result

print(solution())