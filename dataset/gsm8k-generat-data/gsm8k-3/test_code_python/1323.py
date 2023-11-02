def solution():
    """Tony has a piece of quilt that is 6 feet by 24 feet. If he wants to turn it into a square and use all the fabric, how long is each side of the square?"""
    # Calculate the total area of the quilt
    total_area = 6 * 24

    # Calculate the area of one side of the square
    square_area = total_area / 4

    # Calculate the length of one side of the square
    side_length = round((square_area)**0.5,2)

    # Display the length of one side of the square
    result = side_length
    return result

print(solution())