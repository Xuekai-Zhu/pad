def solution():
    # Calculate the length of one side of the square with a perimeter equal to the area of the circle
    # The formula for the area of a circle is A = pi * r^2, and for a square, P = 4s
    # So if A = P, then pi * r^2 = 4s
    # Solving for s, we get s = pi * r^2 / 4 = (3.14 * r^2) / 4

    area_circle = 100
    r = (area_circle / 3.14) ** 0.5  # calculate the radius of the circle using the area
    side_square = (3.14 * r ** 2) / 4  # calculate the length of one side of the square
    result = side_square
    return result

print(solution())