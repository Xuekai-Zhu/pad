def solution():
    """Enrique has 2 132 contracts that he needs to shred.  His paper shredder will only allow him to shred 6 pages at a time.  How many times will he shred 6 units of paper until all of the contracts are shredded?"""
    # Define the number of pages in the contracts
    NUM_PAGES = 2132

    # Calculate the number of times Enrique needs to shred 6 pages
    num_shreds = NUM_PAGES / 6

    # Display the number of times Enrique needs to shred 6 pages
    result = num_shreds
    return result

print(solution())