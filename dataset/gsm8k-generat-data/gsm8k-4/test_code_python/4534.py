def solution():
    """There were 63 Easter eggs in the yard.  Hannah found twice as many as Helen.  How many Easter eggs did Hannah find?"""
    # Define the total number of eggs and the ratio between Hannah's and Helen's eggs
    total_eggs = 63
    hannah_to_helen_ratio = 2

    # Calculate the sum of the ratio
    total_ratio = hannah_to_helen_ratio + 1

    # Calculate the number of eggs Helen found
    helen_eggs = total_eggs / total_ratio

    # Calculate the number of eggs Hannah found
    hannah_eggs = hannah_to_helen_ratio * helen_eggs

    # Return the result
    result = hannah_eggs
    return result

print(solution())