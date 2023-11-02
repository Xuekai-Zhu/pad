def solution():
    """There were 63 Easter eggs in the yard.  Hannah found twice as many as Helen.  How many Easter eggs did Hannah find?"""
    # Define the total number of eggs in the yard
    TOTAL_EGGS = 63

    # Define the number of eggs that Helen found
    helen_eggs = TOTAL_EGGS // 3  # Hannah found twice as many as Helen, so Helen found 1/3 of the total eggs
    # Calculate the number of eggs that Hannah found
    hannah_eggs = helen_eggs * 2

    # Display the number of eggs that Hannah found
    result = hannah_eggs
    return result

print(solution())