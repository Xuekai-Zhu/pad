def solution():
    # Calculate the total number of hours Jeff spends catching up with his Facebook pals
    weekend_catchup = 3 * (3 + 3)  # Jeff spends three times as many hours catching up with his Facebook pals as he does working, and he works for 3 hours every day on the weekends (Saturday and Sunday)
    weekday_work = 4 * 3 * 5  # Jeff spends four times as many hours working as he does catching up, and he works for 3 hours every weekday (Monday-Friday)

    # Calculate the total number of hours Jeff spends working in an entire week
    total_hours = weekend_catchup + weekday_work
    result = total_hours
    return result

print(solution())