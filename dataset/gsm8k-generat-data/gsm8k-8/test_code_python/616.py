def solution():
    # Calculate Kris's balloons in the first 15 minutes
    kris_balloons_15min = 2 * 15

    # Calculate Brother's balloons in the first 15 minutes
    brother_balloons_15min = 4 * 15 / 2

    # Calculate Brother's balloons in the last 15 minutes
    brother_balloons_15_30min = 8 * 15 / 2

    # Calculate total balloons
    total_balloons = kris_balloons_15min + brother_balloons_15min + brother_balloons_15_30min

    result = total_balloons
    return result

print(solution())