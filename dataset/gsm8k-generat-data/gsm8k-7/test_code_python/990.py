def solution():
    mowing_rate = 6
    weeding_rate = 11
    mulching_rate = 9

    mowing_hours = 63
    weeding_hours = 9
    mulching_hours = 10

    # Calculate the total earnings from mowing
    mowing_earnings = mowing_rate * mowing_hours

    # Calculate the total earnings from weeding
    weeding_earnings = weeding_rate * weeding_hours

    # Calculate the total earnings from mulching
    mulching_earnings = mulching_rate * mulching_hours

    # Calculate the total earnings for the month
    total_earnings = mowing_earnings + weeding_earnings + mulching_earnings
    result = total_earnings
    return result

print(solution())