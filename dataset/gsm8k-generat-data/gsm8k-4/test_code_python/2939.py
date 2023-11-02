def solution():
    """Candy throws 4 pebbles into the lake.  Lance throws in 3 times as many pebbles as Candy. How many more pebbles did Lance throw compared to Candy?"""
    # Define the number of pebbles Candy throws
    candy_pebbles = 4

    # Define the number of pebbles Lance throws relative to Candy
    lance_pebbles_ratio = 3

    # Calculate the number of pebbles Lance throws
    lance_pebbles = candy_pebbles * lance_pebbles_ratio

    # Calculate the difference in the number of pebbles thrown by Lance and Candy
    pebbles_difference = lance_pebbles - candy_pebbles

    # Display the result
    result = pebbles_difference
    return result

print(solution())