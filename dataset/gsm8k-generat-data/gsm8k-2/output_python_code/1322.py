def solution():
    """Tony has a piece of quilt that is 6 feet by 24 feet. If he wants to turn it into a square and use all the fabric, how long is each side of the square?"""
    quilt_length = 24
    quilt_width = 6
    quilt_area = quilt_length * quilt_width
    square_side = quilt_area ** 0.5
    result = square_side
    return result

print(solution())