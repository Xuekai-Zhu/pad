def solution():
    """Jeff spends three times as many hours on the weekend catching up with his Facebook pals as he does working.
    Monday through Friday, however, he spends four times as many hours working as he does catching up.
    If he spends 3 hours every day catching up, how many hours does he spend working in an entire week?"""
    # Define the hours spent catching up on the weekend and during weekdays
    weekend_catchup_hours = 3 * working_hours
    weekday_catchup_hours = 3 * 5 * 3  # 3 hours a day for 5 weekdays

    # Define the hours spent working during weekdays
    weekday_working_hours = 4 * weekday_catchup_hours

    # Define the total hours worked in a week
    total_hours = weekend_catchup_hours + weekday_catchup_hours + weekday_working_hours

    # Display the total hours worked in a week
    return total_hours

print(solution())