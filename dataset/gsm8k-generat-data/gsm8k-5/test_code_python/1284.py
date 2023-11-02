def solution():
    shower_time = 10  # John takes a 10-minute shower
    frequency = 0.5  # John showers every other day
    weeks = 4  # John wants to know how much water he uses in 4 weeks
    water_per_minute = 2  # John's shower uses 2 gallons of water per minute

    # Calculate the total number of showers John takes in 4 weeks
    total_showers = frequency * 7 * weeks

    # Calculate the total time John spends showering in 4 weeks
    total_shower_time = total_showers * shower_time

    # Calculate the total water John uses in 4 weeks
    total_water_used = total_shower_time * water_per_minute

    result = total_water_used
    return result

print(solution())