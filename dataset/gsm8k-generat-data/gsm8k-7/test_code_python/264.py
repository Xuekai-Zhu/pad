def solution():
    weekday_earnings = 600
    weekend_earnings = weekday_earnings * 2
    num_weekdays = 22 #assuming there are 22 weekdays in a month
    num_weekends = 8 #assuming there are 8 weekends in a month

    # Calculate the total earnings from weekdays and weekends
    total_earnings = (weekday_earnings * num_weekdays) + (weekend_earnings * num_weekends)

    result = total_earnings
    return result

print(solution())