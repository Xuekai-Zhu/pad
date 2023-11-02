def solution():
    # Calculate earnings from weekdays
    weekday_earnings = 5 * 3 * 5 

    # Calculate earnings from weekends
    weekend_earnings = 3 * 2 * (3 + 4) 

    # Calculate total earnings for the week
    total_earnings = weekday_earnings + weekend_earnings

    result = total_earnings
    return result

print(solution())