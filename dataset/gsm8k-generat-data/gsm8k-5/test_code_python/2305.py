def solution():
    total_length = 40  # The rope is 40 meters long
    ratio_parts = 2 + 3  # The ratio of the two parts is 2:3, so the parts are in a 2+3=5 ratio
    shorter_part_ratio = 2  # The shorter part is in a 2:3 ratio

    # Calculate the length of the shorter part
    shorter_part_length = (total_length / ratio_parts) * shorter_part_ratio
    result = shorter_part_length
    return result

print(solution())