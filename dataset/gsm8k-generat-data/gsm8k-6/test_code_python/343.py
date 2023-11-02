def solution():
    # Calculate the total electricity used by Kim's TV in a week
    weekly_electricity = 125 * 4 * 7  # 125 watts used per hour, TV runs for 4 hours a day, for 7 days in a week
    weekly_kwh = weekly_electricity / 1000  # convert watts to kilowatts
    weekly_cost = weekly_kwh * 14  # cost of electricity is 14 cents per kilowatt hour
    result = weekly_cost
    return result

print(solution())