def solution():
    """Elliott drew a right-angle triangle on his book. It had a base of 4 inches, a height of 3 inches and a certain length of the hypotenuse. What was the length of the perimeter of the triangle that he drew?"""
    # Define the dimensions of the triangle
    base = 4
    height = 3
    hypotenuse = ((base ** 2) + (height ** 2)) ** 0.5

    # Calculate the length of the perimeter
    perimeter = base + height + hypotenuse

    result = perimeter
    return result

print(solution())