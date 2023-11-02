def solution():
    """Five less than three times the number of Doberman puppies plus the difference 
    between the number of Doberman puppies and the number of Schnauzers is equal to 90.
    If the number of Doberman puppies is 20, how many Schnauzers are there?"""
    # Define the number of Doberman puppies
    doberman_puppies = 20

    # Set up the equation
    # 3 * doberman_puppies - 5 + (doberman_puppies - schnauzers) = 90
    # 4 * doberman_puppies - schnauzers = 95
    schnauzers = 4 * doberman_puppies - 95

    # Display the number of Schnauzers
    result = schnauzers
    return result

print(solution())