def solution():
    daily_consumption = 12  # Ada's daily electric consumption is 12 kilowatts per hour
    new_consumption = 2  # Ada is planning to add a device will consume 2 kilowatts per hour a day
    hourly_rate = 1.5  # Ada's hourly rate is $1.50
    days_in_week = 7  # Ada is planning to add a weekly electric bill

    # Calculate Ada's weekly electric consumption before and after adding the new device
    weekly_consumption_before = daily_consumption * days_in_week

    # Calculate Ada's weekly electric consumption after adding the new device
    weekly_consumption_after = weekly_consumption * hourly_rate * days_in_week

    # Calculate the difference between Ada's weekly electric consumption and the new device consumption
    difference = weekly_consumption_before - weekly_consumption_after
    result = difference
    return result

print(solution())