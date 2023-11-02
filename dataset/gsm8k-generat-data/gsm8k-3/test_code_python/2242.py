def solution():
    """Xavier runs three times as many miles as Katie, who runs 4 times as many miles as Cole. If Xavier runs 84 miles, how many miles does Cole run?"""
    # Define the number of miles Cole runs as variable c
    c = 1

    # Define the number of miles Katie runs as variable k, based on the relation to Cole's miles
    k = 4 * c

    # Define the number of miles Xavier runs as variable x, based on the relation to Katie's miles
    x = 3 * k

    # Set the number of miles Xavier runs to be 84 and solve for Cole's miles
    c = 84 / (3 * 4 * 1)

    # Display Cole's number of miles
    result = c
    return result

print(solution())