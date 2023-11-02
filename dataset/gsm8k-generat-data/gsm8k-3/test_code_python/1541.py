def solution():
    """Avery opens a flower shop. She ties 8 bunches of flowers with 9 flowers in each bunch. How many bunches would she have if she put 12 flowers in each bunch instead?"""
    # Define the initial number of bunches and flowers per bunch
    initial_bunches = 8
    initial_flowers = 9

    # Define the desired number of flowers per bunch
    desired_flowers = 12

    # Calculate the new number of bunches
    new_bunches = initial_bunches * (initial_flowers / desired_flowers)

    # Display the new number of bunches
    result = new_bunches
    return result

print(solution())