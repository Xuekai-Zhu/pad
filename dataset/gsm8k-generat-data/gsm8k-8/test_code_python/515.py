def solution():
    # Calculate the number of degrees below freezing
    degrees_below_freezing = 32 - 8

    # Calculate the number of 3-degree intervals below freezing
    intervals_below_freezing = degrees_below_freezing // 3

    # Calculate the percentage increase in skid risk for each interval
    skid_increase_per_interval = 0.05

    # Calculate the total percentage increase in skid risk
    total_skid_increase = skid_increase_per_interval * intervals_below_freezing

    # Calculate the total skid risk
    skid_risk = 0.4 + total_skid_increase

    # Calculate the percentage chance of a serious accident
    serious_accident_chance = 100 - (skid_risk * 100)

    result = serious_accident_chance
    return result

print(solution())