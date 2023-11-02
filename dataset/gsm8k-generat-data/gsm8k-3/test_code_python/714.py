def solution():
    """John runs a website that gets 30000 visits a month, for a normal 30 day month.  He gets $.01 per visit.  How much does he make per day?"""
    # Define the number of visits and the earning per visit
    VISITS = 30000
    EARNING_PER_VISIT = 0.01

    # Calculate the total earnings in a month
    total_earnings = VISITS * EARNING_PER_VISIT

    # Calculate the earnings per day
    earnings_per_day = total_earnings / 30

    # Display the earnings per day
    result = earnings_per_day
    return result

print(solution())