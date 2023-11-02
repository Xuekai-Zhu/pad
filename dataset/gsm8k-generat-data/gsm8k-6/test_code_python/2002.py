def solution():
    # Calculate the number of circles and squares on Pete's flag
    num_stars = 50  # number of stars on US flag
    num_stripes = 13  # number of stripes on US flag
    num_circles = (num_stars // 2) - 3  # circles represent ice cream scoops
    num_squares = 2*num_stripes + 6  # squares represent hidden brownies
    total_shapes = num_circles + num_squares
    result = total_shapes
    return result

print(solution())