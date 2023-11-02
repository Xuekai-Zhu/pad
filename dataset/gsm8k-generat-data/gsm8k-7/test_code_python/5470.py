def solution():
    perfect_shells = 17
    broken_shells = 52

    perfect_nonspiral = 12
    broken_spiral = broken_shells / 2

    perfect_spiral = perfect_shells - perfect_nonspiral
    broken_nonspiral = broken_shells - broken_spiral

    # Calculate the difference between broken spiral and perfect spiral shells
    difference = broken_spiral - perfect_spiral
    result = difference
    return result

print(solution())