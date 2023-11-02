def solution():
    # Calculate the earnings from weekdays
    weekday_earnings = 600 * 5

    # Calculate the earnings from weekends
    weekend_earnings = 2 * 600 * 2

    # Calculate the total earnings for the month
    total_earnings = weekday_earnings + weekend_earnings

    result = total_earnings
    return result

print(solution())