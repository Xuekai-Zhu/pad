def solution():
    sick_days = 10  # sick days per year
    vacation_days = 10  # vacation days per year
    # Mark uses half of each type of days, so he uses 5 of each
    used_sick_days = 5
    used_vacation_days = 5
    # Calculate the number of hours worth of days Mark has left
    remaining_sick_days = sick_days - used_sick_days
    remaining_vacation_days = vacation_days - used_vacation_days
    total_hours_left = (remaining_sick_days + remaining_vacation_days) * 8
    result = total_hours_left
    return result

print(solution())