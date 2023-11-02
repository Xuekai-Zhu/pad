def solution():
    """Sally and Bob have made plans to go on a trip at the end of the year. They both decide to work as babysitters and save half of what they've earned for their trip. If Sally makes $6 per day and Bob makes $4 per day, how much money will they both have saved for their trip after a year?"""
    # Define the number of days in a year
    DAYS_IN_YEAR = 365

    # Define the earnings per day for Sally and Bob
    sally_earnings_per_day = 6
    bob_earnings_per_day = 4

    # Calculate the total earnings for Sally and Bob
    sally_earnings = sally_earnings_per_day * DAYS_IN_YEAR
    bob_earnings = bob_earnings_per_day * DAYS_IN_YEAR

    # Calculate the total amount saved for the trip by Sally and Bob
    total_savings = (sally_earnings + bob_earnings) / 2

    result = total_savings
    return result

print(solution())