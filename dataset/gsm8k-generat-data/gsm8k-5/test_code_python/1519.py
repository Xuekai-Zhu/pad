def solution():
    hourly_wage = 15  # Sandy earns $15 per hour
    friday_hours = 10  # Sandy worked 10 hours on Friday
    saturday_hours = 6  # Sandy worked 6 hours on Saturday
    sunday_hours = 14  # Sandy worked 14 hours on Sunday

    # Calculate the total earnings for each day
    friday_earnings = hourly_wage * friday_hours
    saturday_earnings = hourly_wage * saturday_hours
    sunday_earnings = hourly_wage * sunday_hours

    # Calculate the total earnings for all three days
    total_earnings = friday_earnings + saturday_earnings + sunday_earnings
    result = total_earnings
    return result

print(solution())