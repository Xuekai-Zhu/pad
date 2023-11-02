def solution():
    # Calculate the number of pieces of sea glass found by Dorothy
    red_glass_d = 2 * (12 + 9)  # Dorothy found twice as many pieces of red glass as Blanche and Rose
    blue_glass_d = 3 * 11  # Dorothy found three times as much blue sea glass as Rose
    green_glass_d = 0  # No green sea glass found by Dorothy
    total_glass_d = red_glass_d + blue_glass_d + green_glass_d

    result = total_glass_d
    return result

print(solution())