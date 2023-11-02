def solution():
    # Calculate the number of apples packed in the first week
    packed_first_week = 40 * 50 * 7

    # Calculate the number of apples packed in the second week
    packed_second_week = (40 - 500/50) * 50 * 7

    # Calculate the total number of apples packed
    total_packed = packed_first_week + packed_second_week
    result = total_packed
    return result

print(solution())