def solution():
    # Calculate the total commute time on weekdays
    weekday_commute = 2 * 30  # Sherman commutes 30 minutes each way

    # Calculate the total driving time on weekends
    weekend_driving = 2 * 2  # Sherman spends 2 hours each day driving his kids

    # Calculate the total driving time for the week
    total_driving = weekday_commute + weekend_driving

    # Convert the total driving time to hours
    hours_driven = total_driving / 60
    result = hours_driven
    return result

print(solution())