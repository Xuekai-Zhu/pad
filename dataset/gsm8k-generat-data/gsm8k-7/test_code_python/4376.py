def solution():
    # Calculate the total number of hours Austin worked
    total_hours_worked = 2 + 1 + 3

    # Calculate Austin's total earnings
    earnings_per_hour = 5.0
    total_earnings = earnings_per_hour * total_hours_worked

    # Calculate the number of weeks needed to earn enough for the bicycle
    bike_cost = 180
    weeks_needed = bike_cost / total_earnings
    result = weeks_needed
    return result

print(solution())