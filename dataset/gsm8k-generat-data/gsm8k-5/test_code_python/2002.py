def solution():
    # Calculate the number of stars and stripes on the US flag
    num_stars = 50
    num_stripes = 13

    # Calculate the number of circles and squares on Pete's flag
    num_circles = (num_stars / 2) - 3
    num_squares = (2 * num_stripes) + 6

    # Calculate the combined total of circles and squares on Pete's flag
    total_shapes = num_circles + num_squares
    result = total_shapes
    return result

print(solution())