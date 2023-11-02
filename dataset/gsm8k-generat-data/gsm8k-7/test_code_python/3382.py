def solution():
    days_worked = 300
    march_days_off = 5
    september_days_off = 2 * march_days_off

    # Calculate the total number of vacation days earned
    vacation_days_earned = days_worked // 10

    # Calculate the total number of days Andrew took off
    total_days_off = march_days_off + september_days_off

    # Calculate the remaining vacation days Andrew can still take
    remaining_vacation_days = vacation_days_earned - total_days_off
    result = remaining_vacation_days
    return result

print(solution())