def solution():
    import math

    base = 4
    height = 3
    hypotenuse = math.sqrt(base**2 + height**2)

    perimeter = base + height + hypotenuse
    result = perimeter
    return result

print(solution())