def solution():
    hourly_rate = 10

    hours_worked_monday = 7
    tips_monday = 18

    hours_worked_tuesday = 5
    tips_tuesday = 12

    hours_worked_wednesday = 7
    tips_wednesday = 20

    # Calculate the total amount earned from the hourly rate
    total_hourly_earnings = (hours_worked_monday + hours_worked_tuesday + hours_worked_wednesday) * hourly_rate

    # Calculate the total amount earned from tips
    total_tip_earnings = tips_monday + tips_tuesday + tips_wednesday

    # Calculate the total amount earned
    total_earnings = total_hourly_earnings + total_tip_earnings
    result = total_earnings
    return result

print(solution())