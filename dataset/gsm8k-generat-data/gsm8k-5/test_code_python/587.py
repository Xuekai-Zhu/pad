def solution():
    # Hours spent catching up on the weekend
    weekend_catchup = 3 * 3  # Jeff spends three times as many hours catching up on the weekend as he does working

    # Hours spent catching up on weekdays
    weekday_catchup = 3 * 4 * 5  # Jeff spends four times as many hours working as he does catching up, for 5 days a week

    # Total hours spent working in a week
    total_working_hours = weekday_catchup + weekend_catchup
    result = total_working_hours
    return result

print(solution())