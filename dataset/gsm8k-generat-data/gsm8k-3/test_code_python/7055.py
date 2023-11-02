def solution():
    """Cindy had 20 marbles which is 5 more than what Lisa had. If Cindy gave her 12 marbles, how many more marbles does Lisa have now?"""
    # Define the initial number of marbles Cindy had
    cindy_initial = 20

    # Define the initial number of marbles Lisa had
    lisa_initial = cindy_initial - 5

    # Cindy gives 12 marbles to Lisa
    cindy_final = cindy_initial - 12
    lisa_final = lisa_initial + 12

    # Calculate how many more marbles Lisa has now than before
    more_marbles = lisa_final - lisa_initial

    # Display the result
    result = more_marbles
    return result

print(solution())