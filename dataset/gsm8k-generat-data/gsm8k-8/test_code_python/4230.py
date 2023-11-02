def solution():
    water_used = (6 * 5) + (4 * 8)
    remaining_water = 122 - water_used

    max_num_fours = remaining_water // 4

    result = max_num_fours
    return result

print(solution())