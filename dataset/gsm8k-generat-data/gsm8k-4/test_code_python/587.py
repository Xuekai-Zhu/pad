def solution():
    """Jeff spends three times as many hours on the weekend catching up with his Facebook pals as he does working. Monday through Friday, however, he spends four times as many hours working as he does catching up. If he spends 3 hours every day catching up, how many hours does he spend working in an entire week?"""
    # Define Jeff's catching up time on weekdays and weekends
    catching_up_weekdays = 3
    catching_up_weekends = catching_up_weekdays * 3

    # Define Jeff's working time on weekdays and weekends
    working_weekdays = catching_up_weekdays * 4
    working_weekends = 0

    # Calculate Jeff's total working hours in a week
    total_working_hours = (working_weekdays + working_weekends) * 5

    # return the result
    result = total_working_hours
    return result

print(solution())