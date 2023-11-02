def solution():
    """Cristine bought a dozen lemons and gave 1/4 of them to her neighbor. How many lemons does Cristine have left?"""
    # Define the initial number of lemons
    initial_lemons = 12

    # Calculate the number of lemons Cristine gave to her neighbor
    neighbor_lemons = initial_lemons * 1/4

    # Calculate the number of lemons Cristine has left
    remaining_lemons = initial_lemons - neighbor_lemons

    # Display the remaining number of lemons
    result = remaining_lemons
    return result

print(solution())