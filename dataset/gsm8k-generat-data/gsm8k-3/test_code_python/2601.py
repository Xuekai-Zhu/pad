def solution():
    """James made $4000 in January.  The next month he made twice as much.  In March, however, James made $2000 less than in February.  How much has James made so far this year?"""
    # Calculate James' earnings for February and March
    earnings_feb = 4000 * 2
    earnings_mar = earnings_feb - 2000

    # Calculate James' total earnings for the year
    total_earnings = 4000 + earnings_feb + earnings_mar

    # Display James' total earnings for the year
    result = total_earnings
    return result

print(solution())