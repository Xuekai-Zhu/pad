def solution():
    """Cindy had 20 marbles which is 5 more than what Lisa had. If Cindy gave her 12 marbles, how many more marbles does Lisa have now?"""
    # Define the initial number of marbles Cindy had
    cindy_initial = 20

    # Calculate the initial number of marbles Lisa had
    lisa_initial = cindy_initial - 5

    # Cindy gives 12 marbles to Lisa
    cindy_final = cindy_initial - 12
    lisa_final = lisa_initial + 12

    # Calculate the difference in the number of marbles Lisa has now compared to before
    difference = lisa_final - lisa_initial

    # return the result
    result = difference
    return result

print(solution())