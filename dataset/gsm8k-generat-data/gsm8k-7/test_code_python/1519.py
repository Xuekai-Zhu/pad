def solution():
    hourly_wage = 15

    friday_hours = 10
    saturday_hours = 6
    sunday_hours = 14

    # Calculate the total earnings for each day
    friday_earnings = friday_hours * hourly_wage
    saturday_earnings = saturday_hours * hourly_wage
    sunday_earnings = sunday_hours * hourly_wage

    # Calculate the total earnings for all three days
    total_earnings = friday_earnings + saturday_earnings + sunday_earnings
    result = total_earnings
    return result

print(solution())