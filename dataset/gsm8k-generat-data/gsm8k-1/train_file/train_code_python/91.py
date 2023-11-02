def solution():
    """Sally and Bob have made plans to go on a trip at the end of the year. They both decide to work as babysitters and save half of what they've earned for their trip. If Sally makes $6 per day and Bob makes $4 per day, how much money will they both have saved for their trip after a year?"""
    days_per_year = 365
    sally_earnings = 6 * days_per_year
    bob_earnings = 4 * days_per_year
    total_earnings = sally_earnings + bob_earnings
    trip_savings = total_earnings / 2
    result = trip_savings
    return result

print(solution())