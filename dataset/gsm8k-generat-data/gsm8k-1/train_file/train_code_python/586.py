def solution():
    """Jeff spends three times as many hours on the weekend catching up with his Facebook pals as he does working. Monday through Friday, however, he spends four times as many hours working as he does catching up. If he spends 3 hours every day catching up, how many hours does he spend working in an entire week?"""
    weekend_catch_up_hours = 3 * 3 # He spends 3 times as many hours catching up on weekends
    weekday_working_hours = 4 * 3 # He spends four times as many hours working during weekdays
    total_weekday_hours = weekday_working_hours * 5 # He works for 5 days in a week
    total_weekend_hours = weekend_catch_up_hours * 2 # He catches up on weekends for 2 days
    total_hours = total_weekday_hours + total_weekend_hours
    result = total_hours
    return result

print(solution())