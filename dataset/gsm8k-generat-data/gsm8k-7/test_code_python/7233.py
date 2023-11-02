def solution():
    num_total_butterflies = 19
    num_blue_butterflies = 6
    num_yellow_butterflies = num_blue_butterflies / 2

    # Calculate the total number of black butterflies
    num_black_butterflies = num_total_butterflies - num_blue_butterflies - num_yellow_butterflies

    result = num_black_butterflies
    return result

print(solution())