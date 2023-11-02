def solution():
    
    base = 4
    height = 3
    hypotenuse = ((base ** 2) + (height ** 2)) ** 0.5
    perimeter = base + height + hypotenuse
    result = perimeter
    return result

print(solution())