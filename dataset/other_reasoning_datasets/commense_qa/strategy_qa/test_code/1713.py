def solution():
    # Define the different cycles: solar, lunar, and daily
    solar_cycle = "year"
    lunar_cycle = "month"
    daily_cycle = "day"
    # Check if months are based on the solar cycle
    if lunar_cycle != solar_cycle:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())