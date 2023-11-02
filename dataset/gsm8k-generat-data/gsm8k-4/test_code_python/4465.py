def solution():
    """June found 2 birds nest with 5 eggs each in 1 tree and 1 nest with 3 eggs in another tree. There was also a nest with 4 eggs in her front yard. How many birds eggs did she find?"""
    # Calculate the number of eggs in the first two nests
    eggs_in_nests_1_2 = 2 * 5

    # Calculate the total number of eggs
    total_eggs = eggs_in_nests_1_2 + 3 + 4

    # Return the result
    result = total_eggs
    return result

print(solution())