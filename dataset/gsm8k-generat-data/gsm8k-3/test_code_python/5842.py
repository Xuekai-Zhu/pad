def solution():
    """James streams on twitch.  He had 150 subscribers and then someone gifted 50 subscribers.  If he gets $9 a month per subscriber how much money does he make a month?"""
    # Define the number of subscribers and the subscription price
    num_subscribers = 150 + 50
    subscription_price = 9

    # Calculate James' monthly income
    monthly_income = num_subscribers * subscription_price

    # Display James' monthly income
    result = monthly_income
    return result

print(solution())