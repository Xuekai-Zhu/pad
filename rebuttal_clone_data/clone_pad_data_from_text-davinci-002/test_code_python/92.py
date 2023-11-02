def solution():
    """Sally and Bob have made plans to go on a trip at the end of the year. They both decide to work as babysitters and save half of what they've earned for their trip. If Sally makes $6 per day and Bob makes $4 per day, how much money will they both have saved for their trip after a year?"""
    sally_daily_rate = 6
    bob_daily_rate = 4
    days_per_year = 365
    sally_savings = (sally_daily_rate * days_per_year) / 2
    bob_savings = (bob_daily_rate * days_per_year) / 2
    total_savings = sally_savings + bob_savings
    result = total_savings
    return result

print(solution())