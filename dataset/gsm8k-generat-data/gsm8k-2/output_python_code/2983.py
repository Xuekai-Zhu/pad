def solution():
    """Joshua packs 12 bottles in each crate. He has a total of 130 bottles and 10 crates. How many bottles will not be placed in a crate?"""
    bottles = 130
    crates = 10
    bottles_in_crates = crates * 12
    remaining_bottles = bottles - bottles_in_crates
    result = remaining_bottles
    return result

print(solution())