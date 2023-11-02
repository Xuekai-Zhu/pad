def solution():
    grant_yearly_cost = 200.0

    daily_cost_mon_sat = 0.5
    daily_cost_sun = 2.0

    num_weekdays = 6
    num_sundays = 1

    # Calculate the total cost of buying the newspaper daily for a year
    total_daily_cost = (num_weekdays * daily_cost_mon_sat + num_sundays * daily_cost_sun) * 365

    # Calculate the difference between Juanita's total cost and Grant's cost
    difference = total_daily_cost - grant_yearly_cost
    result = difference
    return result

print(solution())