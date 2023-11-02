def solution():
    hourly_rate = 9
    monday_hours = 4
    wednesday_hours = 3
    friday_hours = 6

    # Calculate the total hours worked
    total_hours = monday_hours + wednesday_hours + friday_hours

    # Calculate Olivia's total earnings
    total_earnings = total_hours * hourly_rate
    result = total_earnings
    return result

print(solution())