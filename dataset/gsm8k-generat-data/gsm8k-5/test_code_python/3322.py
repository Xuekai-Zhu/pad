def solution():
    total_speed = 59 * 5  # Tony's total speed during the day was his average speed multiplied by number of rollercoasters
    speed_first_four = 50 + 62 + 73 + 70  # Tony's speed on the first four rollercoasters
    speed_fifth_coaster = (total_speed - speed_first_four) / 1  # Tony's speed on the fifth rollercoaster, assuming he went on only 5 rollercoasters

    result = speed_fifth_coaster
    return result

print(solution())