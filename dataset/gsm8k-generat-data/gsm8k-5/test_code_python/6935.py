def solution():
    # Calculate the kilowatt-hours consumed per hour
    kwh_per_hour = 7.2 / 8  # 7.2 kilowatts consumed in 8 hours

    # Calculate the total kilowatt-hours consumed over 5 days
    total_hours = 6 * 5  # Air conditioner is used for 6 hours a day for 5 days
    total_kwh = kwh_per_hour * total_hours

    result = total_kwh
    return result

print(solution())