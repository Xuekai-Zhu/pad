def solution():
    """Janet has 24 dresses.  Half of them have pockets.  Of those, a third have 2 pockets and the rest have 3 pockets.  How many total pockets do her dresses have?"""
    # Define the number of dresses
    NUM_DRESSES = 24

    # Calculate the number of dresses with pockets
    pocket_dresses = NUM_DRESSES / 2

    # Calculate the number of dresses with 2 pockets and 3 pockets
    pockets_2 = pocket_dresses / 3
    pockets_3 = pocket_dresses - pockets_2

    # Calculate the total number of pockets
    total_pockets = (pockets_2 * 2) + (pockets_3 * 3)

    # Display the total number of pockets
    result = total_pockets
    return result

print(solution())