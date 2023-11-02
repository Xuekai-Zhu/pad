def solution():
    """Tom catches crabs for a living.  He has 8 crab buckets that he checks every day.  Each crab bucket gets 12 crabs.  He sells each of these crabs for $5 each.  How much money does he make per week?"""
    # Define the number of crab buckets and number of crabs per bucket
    CRAB_BUCKETS = 8
    CRABS_PER_BUCKET = 12

    # Calculate the total number of crabs caught per day
    crabs_per_day = CRAB_BUCKETS * CRABS_PER_BUCKET

    # Calculate the total revenue generated per day
    revenue_per_day = crabs_per_day * 5

    # Calculate the total revenue generated per week
    revenue_per_week = revenue_per_day * 7

    # Display the total revenue generated per week
    result = revenue_per_week
    return result

print(solution())