def solution():
    base = 4  # inches
    height = 3  # inches
    
    # Calculate the length of the hypotenuse using Pythagorean theorem
    hypotenuse = ((base**2) + (height**2))**0.5  # inches
    
    # Calculate the perimeter of the triangle
    perimeter = base + height + hypotenuse  # inches
    result = perimeter
    return result

print(solution())