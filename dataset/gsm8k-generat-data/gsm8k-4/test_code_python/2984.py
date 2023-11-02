def solution():
    """Joshua packs 12 bottles in each crate. He has a total of 130 bottles and 10 crates. How many bottles will not be placed in a crate?"""
    # Define the number of bottles and crates
    total_bottles = 130
    crates = 10

    # Calculate the total number of bottles that can be placed in the crates
    bottles_in_crates = crates * 12

    # Calculate the remainder of bottles not placed in a crate
    remainder_bottles = total_bottles - bottles_in_crates

    # return the result
    result = remainder_bottles
    return result

print(solution())