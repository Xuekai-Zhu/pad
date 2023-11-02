def solution():
    num_stars = 50
    num_stripes = 13

    # Calculate the number of circles
    num_circles = (num_stars / 2) - 3

    # Calculate the number of squares
    num_squares = (2 * num_stripes) + 6

    # Calculate the combined total of circles and squares
    total_shapes = num_circles + num_squares
    
    result = total_shapes
    return result

print(solution())