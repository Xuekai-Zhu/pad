def solution():
    """Johnny is a dog walker. He can walk 3 dogs at once. He gets paid $15 for a 30-minute walk and $20 for a 60-minute walk. Johnny works for 4 hours per day. If he always walks the maximum number of dogs possible and 6 dogs have 60-minute walks per day, how much money does he make in a week where he works 5 days?"""
    # Define the pay rates
    RATE_30_MIN = 15
    RATE_60_MIN = 20

    # Define the number of dogs Johnny can walk at once
    MAX_DOGS = 3

    # Define the length of Johnny's workday in minutes
    WORKDAY_MINUTES = 4 * 60

    # Calculate the number of 30-minute walks Johnny can take in a workday
    walks_30 = WORKDAY_MINUTES // 30

    # Calculate the number of 60-minute walks Johnny can take in a workday
    walks_60 = 0

    # If there are dogs with 60-minute walks, subtract the time for those walks from Johnny's workday
    if walks_30 > 6:
        walks_60 = 6
        WORKDAY_MINUTES -= walks_60 * 60

    # Calculate the remaining number of 30-minute walks Johnny can take
    walks_30 = WORKDAY_MINUTES // 30

    # Calculate the total amount Johnny earns in one workday
    earnings = (walks_30 * RATE_30_MIN) + (walks_60 * RATE_60_MIN)

    # Calculate the total amount Johnny earns in one week
    weekly_earnings = earnings * 5

    # Display the total amount Johnny earns in one week
    result = weekly_earnings
    return result

print(solution())