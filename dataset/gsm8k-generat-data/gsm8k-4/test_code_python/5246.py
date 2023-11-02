def solution():
    """Greg has his own dog walking business. He charges $20 per dog plus $1 per minute per dog for walking the dog. If he walks one dog for 10 minutes, two dogs for 7 minutes and three dogs for 9 minutes, how much money, in dollars, does he earn?"""
    # Define the per-dog price and per-minute price
    PER_DOG_PRICE = 20
    PER_MINUTE_PRICE = 1

    # Define the number of dogs and minutes walked for each session
    session_1_dogs = 1
    session_1_minutes = 10
    session_2_dogs = 2
    session_2_minutes = 7
    session_3_dogs = 3
    session_3_minutes = 9

    # Calculate the earnings for each session
    session_1_earnings = (session_1_dogs * PER_DOG_PRICE) + (session_1_minutes * session_1_dogs * PER_MINUTE_PRICE)
    session_2_earnings = (session_2_dogs * PER_DOG_PRICE) + (session_2_minutes * session_2_dogs * PER_MINUTE_PRICE)
    session_3_earnings = (session_3_dogs * PER_DOG_PRICE) + (session_3_minutes * session_3_dogs * PER_MINUTE_PRICE)

    # Calculate the total earnings
    total_earnings = session_1_earnings + session_2_earnings + session_3_earnings

    # return the result
    result = total_earnings
    return result

print(solution())