def solution():
    # Define the hourly rates for each service
    mowing_rate = 6
    weeding_rate = 11
    mulch_rate = 9

    # Calculate the total earnings for each service
    mowing_earnings = mowing_rate * 63
    weeding_earnings = weeding_rate * 9
    mulch_earnings = mulch_rate * 10

    # Calculate the total earnings for the month
    total_earnings = mowing_earnings + weeding_earnings + mulch_earnings
    result = total_earnings
    return result

print(solution())