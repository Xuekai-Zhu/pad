def solution():
    hourly_rate = 30
    normal_hours = 40
    overtime_rate = 1.5 * hourly_rate

    day1_hours = 6
    day2_hours = 6
    day3_hours = 6
    day4_hours = 2 * day1_hours
    day5_hours = 2 * day2_hours

    # Calculate total hours worked
    total_hours = day1_hours + day2_hours + day3_hours + day4_hours + day5_hours

    # Calculate total earnings for normal hours worked
    normal_earnings = hourly_rate * normal_hours

    # Calculate total earnings for overtime hours worked
    overtime_hours = total_hours - normal_hours
    overtime_earnings = overtime_hours * overtime_rate

    # Calculate total earnings for the week
    total_earnings = normal_earnings + overtime_earnings
    result = total_earnings
    return result

print(solution())