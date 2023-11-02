def solution():
    """Jeff spends three times as many hours on the weekend catching up with his Facebook pals as he does working. Monday through Friday, however, he spends four times as many hours working as he does catching up. If he spends 3 hours every day catching up, how many hours does he spend working in an entire week?"""
    weekend_working_hours = x
    weekend_facebook_hours = 3 * weekend_working_hours
    weekday_working_hours = 4 * 3
    weekday_facebook_hours = 3
    total_working_hours = weekend_working_hours * 2 + weekday_working_hours * 5
    result = total_working_hours
    return result

print(solution())