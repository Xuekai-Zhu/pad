def solution():
    side1 = 16
    side2 = 16
    side3 = 16
    space_per_bush = 4
    total_space = side1 + side2 + side3
    total_bushes = total_space / space_per_bush
    result = total_bushes
    return result

print(solution())