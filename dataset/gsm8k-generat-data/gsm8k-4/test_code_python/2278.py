def solution():
    """Johnny is a dog walker. He can walk 3 dogs at once. He gets paid $15 for a 30-minute walk and $20 for a 60-minute walk. Johnny works for 4 hours per day. If he always walks the maximum number of dogs possible and 6 dogs have 60-minute walks per day, how much money does he make in a week where he works 5 days?"""
    # Define the number of dogs Johnny can walk at once, his hourly rates, and his daily working hours
    MAX_DOGS = 3 
    RATE_30_MIN = 15 
    RATE_60_MIN = 20 
    DAILY_HOURS = 4 

    # Calculate the number of short walks and long walks
    num_long_walks = 6 
    total_dogs = MAX_DOGS * DAILY_HOURS

    # The number of walks Johnny can take
    num_short_walks = (total_dogs - num_long_walks) 
    time_short_walks = num_short_walks * 0.5 
    time_long_walks = num_long_walks * 1 
    total_time = time_short_walks + time_long_walks

    # Calculate Johnny's earnings
    earnings_short_walks = num_short_walks * RATE_30_MIN 
    earnings_long_walks = num_long_walks * RATE_60_MIN
    total_earnings = earnings_short_walks + earnings_long_walks

    # Calculate Johnny's weekly earnings
    weekly_earnings = total_earnings * 5

    result = weekly_earnings
    return result

print(solution())