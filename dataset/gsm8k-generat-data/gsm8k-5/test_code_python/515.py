def solution():
    temp_drop = 8 - 32  # Calculate the temperature drop from 32 degrees
    skid_increase = (temp_drop / 3) * 5  # Calculate the increase in skid chances
    skid_chance = 40 + skid_increase  # Calculate the total skid chance

    # Calculate the percentage chance of a serious accident
    serious_accident_chance = 100 - skid_chance

    result = serious_accident_chance
    return result

print(solution())