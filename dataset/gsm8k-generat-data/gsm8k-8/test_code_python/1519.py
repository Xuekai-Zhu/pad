def solution():
    # Define the hourly rate and hours worked for each day
    friday_rate = 15
    friday_hours = 10
    saturday_rate = 15
    saturday_hours = 6
    sunday_rate = 15
    sunday_hours = 14

    # Calculate Sandy's earnings for each day
    friday_earnings = friday_rate * friday_hours
    saturday_earnings = saturday_rate * saturday_hours
    sunday_earnings = sunday_rate * sunday_hours

    # Calculate Sandy's total earnings
    total_earnings = friday_earnings + saturday_earnings + sunday_earnings
    result = total_earnings
    return result

print(solution())