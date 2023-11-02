def solution():
    """Mark wants to build a pyramid of soda cases that's four levels tall. Each level of the pyramid has a square base where each side is one case longer than the level above it. The top level is just one case. How many cases of soda does Mark need?"""
    # Initialize the variables
    total_cases = 0
    level_cases = 1

    # Calculate the number of cases for each level of the pyramid
    for i in range(1, 5):
        level_cases = i ** 2
        total_cases += level_cases

    # Display the total number of cases needed
    result = total_cases
    return result

print(solution())