def solution():
    # Define the number of marbles Cindy had originally
    cindy_original = 20

    # Calculate the number of marbles Lisa had originally
    lisa_original = cindy_original - 5

    # Calculate the number of marbles Lisa has after Cindy gave her 12
    lisa_new = lisa_original + 12

    # Calculate how many more marbles Lisa has now compared to her original amount
    difference = lisa_new - lisa_original

    result = difference
    return result

print(solution())