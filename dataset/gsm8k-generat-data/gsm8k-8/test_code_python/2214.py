def solution():
    total_time = 150
    math_time = 0.3 * total_time
    science_time = 0.4 * total_time
    other_time = total_time - math_time - science_time
    result = other_time
    return result

print(solution())