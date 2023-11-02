def solution():
    """Mark wants to build a pyramid of soda cases that's four levels tall. Each level of the pyramid has a square base where each side is one case longer than the level above it. The top level is just one case. How many cases of soda does Mark need?"""
    # Define the number of levels in the pyramid
    levels = 4

    # Initialize the number of cases needed to build the pyramid
    total_cases = 0

    # Loop over the levels of the pyramid
    for i in range(levels):
        # Calculate the number of cases needed for this level
        level_cases = (i+1)**2

        # Add the number of cases needed for this level to the total number of cases needed
        total_cases += level_cases

    # Display the total number of cases needed
    result = total_cases
    return result

print(solution())