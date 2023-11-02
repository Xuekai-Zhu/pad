def solution():
    iwato_scale_cases = 5
    chromatic_scale_cases = 12
    if iwato_scale_cases < chromatic_scale_cases:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())