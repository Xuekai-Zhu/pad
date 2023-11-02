def solution():
    # Calculate the kilowatts consumed per hour
    kilowatts_per_hour = 7.2 / 8

    # Calculate the total hours the air conditioner is used
    total_hours = 6 * 5

    # Calculate the total kilowatts consumed
    total_kilowatts = kilowatts_per_hour * total_hours

    result = total_kilowatts
    return result

print(solution())