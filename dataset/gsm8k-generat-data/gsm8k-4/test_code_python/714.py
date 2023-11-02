def solution():
    """John runs a website that gets 30000 visits a month, for a normal 30 day month. He gets $.01 per visit. How much does he make per day?"""
    # Define the number of visits and the rate per visit
    visits_per_month = 30000
    rate_per_visit = 0.01

    # Calculate the total earnings per month
    earnings_per_month = visits_per_month * rate_per_visit

    # Calculate the earnings per day
    earnings_per_day = earnings_per_month / 30

    result = earnings_per_day
    return result

print(solution())