def solution():
    area_circle = 100
    radius = (area_circle / 3.14) ** 0.5  # calculating the radius of the circle
    perimeter_square = 2 * (3.14 * radius)  # calculating the perimeter of the square
    length_of_side = perimeter_square / 4  # calculating the length of one side of the square
    result = length_of_side
    return result

print(solution())