def solution():
    """Sally and Bob have made plans to go on a trip at the end of the year. They both decide to work as babysitters and save half of what they've earned for their trip. If Sally makes $6 per day and Bob makes $4 per day, how much money will they both have saved for their trip after a year?"""
    # Define the daily earnings of Sally and Bob
    sally_daily_earnings = 6
    bob_daily_earnings = 4

    # Calculate the total earnings of Sally and Bob after a year
    sally_total_earnings = sally_daily_earnings * 365
    bob_total_earnings = bob_daily_earnings * 365

    # Calculate the total savings of Sally and Bob after a year
    sally_total_savings = sally_total_earnings / 2
    bob_total_savings = bob_total_earnings / 2

    # Calculate the total savings of Sally and Bob together
    total_savings = sally_total_savings + bob_total_savings

    # Return the result
    result = total_savings
    return result

print(solution())