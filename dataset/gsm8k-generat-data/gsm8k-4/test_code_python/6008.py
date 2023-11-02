def solution():
    """Tom catches crabs for a living. He has 8 crab buckets that he checks every day. Each crab bucket gets 12 crabs. He sells each of these crabs for $5 each. How much money does he make per week?"""
    # Define the number of crab buckets and crabs per bucket
    num_buckets = 8
    crabs_per_bucket = 12

    # Calculate the total number of crabs caught per day
    total_crabs_per_day = num_buckets * crabs_per_bucket

    # Calculate the total earnings per day
    earnings_per_crab = 5
    total_earnings_per_day = total_crabs_per_day * earnings_per_crab

    # Calculate the total earnings per week
    days_per_week = 7
    total_earnings_per_week = total_earnings_per_day * days_per_week

    # return the result
    result = total_earnings_per_week
    return result

print(solution())