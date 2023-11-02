def solution():
    # Calculate John's earnings on Sunday
    sunday_earnings = 18 / 2

    # Calculate John's total earnings for the two weekends
    total_earnings = 18 + sunday_earnings + 20

    # Calculate how much more money John needs to earn to reach $60
    needed_earnings = 60 - total_earnings
    result = needed_earnings
    return result

print(solution())