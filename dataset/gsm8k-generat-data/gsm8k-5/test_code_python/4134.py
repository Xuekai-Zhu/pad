def solution():
    base = 4  # The base of the triangle is 4 inches
    height = 3  # The height of the triangle is 3 inches
    hypotenuse = ((base ** 2) + (height ** 2)) ** 0.5  # Calculate the length of the hypotenuse using Pythagoras' theorem

    # Calculate the perimeter of the triangle
    perimeter = base + height + hypotenuse
    result = perimeter
    return result

print(solution())