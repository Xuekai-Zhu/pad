def solution():
    """In a fundraiser car wash activity, the 5th graders raised $147 on Friday. On Saturday, they made $7 more than twice their Friday earnings. Their earnings on Sunday are $78 more than their earnings on Friday. How much did they earn in three days?"""
    friday_earnings = 147
    saturday_earnings = (2 * friday_earnings) + 7
    sunday_earnings = friday_earnings + 78
    total_earnings = friday_earnings + saturday_earnings + sunday_earnings
    result = total_earnings
    return result

print(solution())