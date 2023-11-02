def solution():
    # Calculate the total number of showers John takes in 4 weeks
    total_showers = 4 * 7 / 2  # 4 weeks, every other day

    # Calculate the total water used in those showers
    water_used = total_showers * 10 * 2  # 10 minutes per shower, 2 gallons of water per minute

    result = water_used
    return result

print(solution())