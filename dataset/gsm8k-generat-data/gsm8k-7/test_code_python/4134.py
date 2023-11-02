def solution():
    base = 4
    height = 3

    # Calculate the length of the hypotenuse using the Pythagorean theorem
    hypotenuse = ((base ** 2) + (height ** 2)) ** 0.5

    # Calculate the perimeter of the triangle
    perimeter = base + height + hypotenuse
    result = perimeter
    return result

print(solution())