def solution():
    
    side_length = 16
    bush_width = 4
    bushes_per_side = side_length / bush_width
    total_bushes = int(bushes_per_side * 3)
    result = total_bushes
    return result

print(solution())