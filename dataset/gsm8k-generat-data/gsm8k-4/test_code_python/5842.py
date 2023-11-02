def solution():
    """James streams on twitch. He had 150 subscribers and then someone gifted 50 subscribers. If he gets $9 a month per subscriber how much money does he make a month?"""
    # Define the initial number of subscribers and the number of gifted subscribers
    initial_subscribers = 150
    gifted_subscribers = 50

    # Calculate the total number of subscribers
    total_subscribers = initial_subscribers + gifted_subscribers

    # Calculate the monthly income from subscribers
    monthly_income = total_subscribers * 9

    # Return the result
    result = monthly_income
    return result

print(solution())