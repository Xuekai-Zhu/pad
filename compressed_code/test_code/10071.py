def solution():
    
    perfect_shells = 17
    broken_shells = 52
    perfect_not_spiral = 12
    broken_spiral = broken_shells / 2
    perfect_spiral = perfect_shells - perfect_not_spiral
    difference = broken_spiral - perfect_spiral
    result = difference
    return result

print(solution())