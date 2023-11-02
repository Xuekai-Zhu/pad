def solution():
    bottles_per_crate = 12  # Joshua packs 12 bottles in each crate
    total_bottles = 130  # Joshua has a total of 130 bottles
    crates = 10  # Joshua has 10 crates

    # Calculate the total number of bottles that will be placed in a crate
    bottles_in_crates = bottles_per_crate * crates

    # Calculate the number of bottles that will not be placed in a crate
    bottles_not_in_crate = total_bottles - bottles_in_crates
    result = bottles_not_in_crate
    return result

print(solution())