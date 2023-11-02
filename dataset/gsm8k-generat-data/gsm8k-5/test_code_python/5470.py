def solution():
    perfect_shells = 17
    broken_shells = 52
    broken_spiral = broken_shells / 2
    perfect_not_spiral = 12

    # Calculate the number of perfect spiral shells
    perfect_spiral = perfect_shells - perfect_not_spiral

    # Calculate the difference between broken spiral shells and perfect spiral shells
    difference = broken_spiral - perfect_spiral
    result = difference
    return result

print(solution())