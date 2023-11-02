def solution():
    """Joshua packs 12 bottles in each crate. He has a total of 130 bottles and 10 crates. How many bottles will not be placed in a crate?"""
    # Define the number of bottles per crate and the total number of crates
    BOTTLES_PER_CRATE = 12
    TOTAL_CRATES = 10

    # Calculate the number of bottles that will be placed in crates
    bottles_in_crates = BOTTLES_PER_CRATE * TOTAL_CRATES

    # Calculate the number of bottles that will not be placed in crates
    bottles_not_in_crates = 130 - bottles_in_crates

    # Display the number of bottles not in crates
    result = bottles_not_in_crates
    return result

print(solution())