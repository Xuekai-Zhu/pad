def solution():
    
    # Define the number of spiders
    spiders = 90

    # Calculate the number of millipedes
    millipedes = spiders / 3

    # Calculate the number of stink bugs
    stink_bugs = 2 * millipedes - 12

    # Calculate the total number of bugs
    total_bugs = spiders + millipedes + stink_bugs

    # Display the total number of bugs
    result = total_bugs
    return result

print(solution())