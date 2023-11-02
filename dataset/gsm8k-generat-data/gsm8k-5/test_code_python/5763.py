def solution():
    friday_earnings = 147  # The 5th graders raised $147 on Friday
    saturday_earnings = 2 * friday_earnings + 7  # On Saturday, they made $7 more than twice their Friday earnings
    sunday_earnings = friday_earnings + 78  # Their earnings on Sunday are $78 more than their earnings on Friday

    # Calculate the total earnings in three days
    total_earnings = friday_earnings + saturday_earnings + sunday_earnings
    result = total_earnings
    return result

print(solution())