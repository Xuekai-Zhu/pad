def solution():
    # Calculate the number of vacation days earned based on number of days worked
    vacation_days_earned = 300 // 10

    # Calculate the number of vacation days used in March and September
    vacation_days_used = 5 + (2 * 5)

    # Calculate the number of remaining vacation days
    remaining_vacation_days = vacation_days_earned - vacation_days_used

    result = remaining_vacation_days
    return result

print(solution())