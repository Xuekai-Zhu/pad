def solution():
    """Tony has a piece of quilt that is 6 feet by 24 feet. If he wants to turn it into a square and use all the fabric, how long is each side of the square?"""
    length = 24
    width = 6
    area = length * width
    side_length = (area)**(1/2)
    result = side_length
    return result

print(solution())