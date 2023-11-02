def solution():
    current_temp = 8
    degrees_below_freezing = 32 - current_temp
    skid_increase_per_3_degrees = 0.05
    skid_chance = 0.4

    # Calculate the percentage increase in skid chance due to temperature
    temp_effect = (degrees_below_freezing // 3) * skid_increase_per_3_degrees

    # Calculate the overall skid chance
    overall_skid_chance = skid_chance + temp_effect

    # Calculate the chance of having a serious accident
    serious_accident_chance = 1 - overall_skid_chance

    # Convert to a percentage
    result = serious_accident_chance * 100
    return result

print(solution())