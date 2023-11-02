def solution():
    watts_per_hour = 125  # Kim's TV uses 125 watts of electricity per hour
    hours_per_day = 4  # Kim runs her TV for 4 hours per day
    days_per_week = 7  # Kim wants to know the cost for 1 week
    kilowatts_per_watt = 0.001  # 1 kilowatt = 1000 watts
    cost_per_kwh = 0.14  # Electricity costs 14 cents per kilowatt hour

    # Calculate the total electricity usage in kilowatt hours for the week
    kwh_per_week = (watts_per_hour * hours_per_day * days_per_week) / (1000)

    # Calculate the total cost for the week in cents
    cost_per_week = kwh_per_week * cost_per_kwh * (100)

    result = cost_per_week
    return result

print(solution())