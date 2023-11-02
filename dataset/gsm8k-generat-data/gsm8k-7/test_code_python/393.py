def solution():
    perimeter = 30
    length = 2 * width

    # Using the formula for the perimeter of a rectangle: 2(length + width) = perimeter
    # Substituting length with 2*width: 2(2*width + width) = perimeter
    # Simplifying: 6*width = perimeter
    # Solving for width: width = perimeter/6
    width = perimeter / 6

    result = width
    return result

print(solution())