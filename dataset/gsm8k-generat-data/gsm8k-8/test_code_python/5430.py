def solution():
    # Calculate the radius of the circle
    radius = (100 / 3.14) ** 0.5

    # Calculate the circumference of the circle
    circumference = 2 * 3.14 * radius

    # Calculate the length of one side of the square
    side_length = circumference / 4
    result = side_length
    return result

print(solution())