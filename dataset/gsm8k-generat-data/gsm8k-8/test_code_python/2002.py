def solution():
    # Define the number of stars and stripes on the US flag
    num_stars = 50
    num_stripes = 13

    # Calculate the number of circles and squares on Pete's flag
    num_circles = (0.5 * num_stars) - 3
    num_squares = (2 * num_stripes) + 6

    # Calculate the combined total number of circles and squares on Pete's flag
    total = num_circles + num_squares
    result = total
    return result

print(solution())