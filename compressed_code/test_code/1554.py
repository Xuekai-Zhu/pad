def solution():
    
    num_stars = 50
    num_stripes = 13
    num_circles = (num_stars // 2) - 3
    num_squares = (2 * num_stripes) + 6
    total_shapes = num_circles + num_squares
    result = total_shapes
    return result

print(solution())