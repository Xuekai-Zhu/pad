def solution():
    lion_daily_consumption = 25
    tiger_daily_consumption = 20
    total_meat = 90

    # Calculate the combined daily consumption of the lion and tiger
    total_daily_consumption = lion_daily_consumption + tiger_daily_consumption

    # Calculate the number of days the meat will last
    num_days = total_meat / total_daily_consumption
    result = num_days
    return result

print(solution())