def solution():
    
    perfect_shells = 17
    broken_shells = 52
    broken_spiral = broken_shells / 2
    perfect_not_spiral = 12
    perfect_spiral = perfect_shells - perfect_not_spiral
    broken_spiral_diff = broken_spiral - perfect_spiral
    result = broken_spiral_diff
    return result

print(solution())