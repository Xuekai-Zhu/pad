def solution():
    blonde_hair = 4
    brown_hair = 4 * 4
    black_hair = brown_hair - 2

    total_non_blonde = brown_hair + black_hair
    difference = total_non_blonde - blonde_hair

    result = difference
    return result

print(solution())