def solution():
    bottles_per_crate = 12
    total_bottles = 130
    num_crates = 10

    # Calculate the total number of bottles that will be placed in crates
    bottles_in_crates = bottles_per_crate * num_crates

    # Calculate the number of bottles that will not be placed in a crate
    bottles_not_in_crate = total_bottles - bottles_in_crates
    result = bottles_not_in_crate
    return result

print(solution())