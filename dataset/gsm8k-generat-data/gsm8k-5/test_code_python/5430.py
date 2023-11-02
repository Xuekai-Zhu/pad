def solution():
    area_circle = 100  # The area of the circle is 100
    radius_circle = ((area_circle / 3.14159) ** 0.5)  # Calculate the radius of the circle using the area formula
    perimeter_square = 2 * 3.14159 * radius_circle  # The perimeter of the square is equal to the perimeter of the circle
    length_side = perimeter_square / 4  # The square has 4 sides, so length of 1 side is perimeter of square / 4
    result = length_side
    return result

print(solution())