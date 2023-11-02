def solution():
    total_length = 80
    crooked_part = total_length / 4  # straight part is 3 times shorter than crooked part
    straight_part = total_length - crooked_part
    result = straight_part
    return result

print(solution())