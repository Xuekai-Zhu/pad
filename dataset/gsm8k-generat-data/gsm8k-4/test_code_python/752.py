def solution():
    """The length of a rectangle is four times its width. If the area is 100 m2. what is the length of the rectangle?"""
    # Define the area of the rectangle
    area = 100

    # Set up the equation for the area of the rectangle
    # A = l * w
    # We know that l = 4w
    # Substitute l = 4w into the equation
    # A = 4w * w = 4w^2
    # Solve for w
    w = (area / 4) ** 0.5

    # Calculate the length of the rectangle
    l = 4 * w

    # Return the length
    result = l
    return result

print(solution())