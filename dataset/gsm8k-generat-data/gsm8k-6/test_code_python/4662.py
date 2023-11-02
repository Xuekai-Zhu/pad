def solution():
    # Calculate Zach's total earnings for the week
    weekly_earnings = 5 + 10 + 7*2  # $5 weekly allowance, $10 for mowing lawn, 2 hours of babysitting at $7 per hour
    # Calculate the total amount Zach will have saved by the end of the week
    total_saved = 65 + weekly_earnings
    # Calculate the difference between the total amount saved and the cost of the bike
    difference = 100 - total_saved
    result = difference
    return result

print(solution())