def solution():
    """Tony has a piece of quilt that is 6 feet by 24 feet. If he wants to turn it into a square and use all the fabric, how long is each side of the square?"""
    # Calculate the total area of the quilt
    total_area = 6 * 24

    # Calculate the length of each side of the square by taking the square root of the total area
    square_side = total_area ** 0.5

    # Round the result to the nearest tenth
    result = round(square_side, 1)
    return result

print(solution())