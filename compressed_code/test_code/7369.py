def solution():
    
    stars_on_US_flag = 50
    stripes_on_US_flag = 13
    circles = (stars_on_US_flag / 2) - 3
    squares = (stripes_on_US_flag * 2) + 6
    total_shapes = circles + squares
    result = total_shapes
    return result

print(solution())