def solution():
    min_temp_citrus = -2
    avg_temp_ulaanbaatar = -0.4
    if avg_temp_ulaanbaatar >= min_temp_citrus:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())