def solution():
    sick_days = 10  # Mark gets 10 sick days per year
    vacation_days = 10  # Mark gets 10 vacation days per year

    # Calculate how many days Mark has left
    remaining_sick_days = sick_days/2
    remaining_vacation_days = vacation_days/2

    # Calculate how many hours' worth of days Mark has left
    total_hours_left = (remaining_sick_days + remaining_vacation_days) * 8
    result = total_hours_left
    return result

print(solution())