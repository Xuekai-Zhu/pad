def solution():
    hourly_rate = 12
    minutes_worked = 50

    # Convert minutes to hours
    hours_worked = minutes_worked / 60

    # Calculate the total earnings
    total_earnings = hourly_rate * hours_worked
    result = total_earnings
    return result

print(solution())