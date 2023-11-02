def solution():
    """Elliott drew a right-angle triangle on his book. It had a base of 4 inches, a height of 3 inches and a certain length of the hypotenuse. What was the length of the perimeter of the triangle that he drew?"""
    # Define the base and height of the triangle
    base = 4
    height = 3

    # Calculate the length of the hypotenuse using the Pythagorean theorem
    hypotenuse = ((base ** 2) + (height ** 2)) ** 0.5

    # Calculate the perimeter of the triangle
    perimeter = base + height + hypotenuse

    # Display the perimeter of the triangle
    result = perimeter
    return result

print(solution())