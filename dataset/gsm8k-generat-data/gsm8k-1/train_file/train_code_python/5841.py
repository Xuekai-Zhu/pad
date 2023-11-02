def solution():
    """James streams on twitch. He had 150 subscribers and then someone gifted 50 subscribers. If he gets $9 a month per subscriber how much money does he make a month?"""
    initial_subscribers = 150
    gifted_subscribers = 50
    total_subscribers = initial_subscribers + gifted_subscribers
    subscription_cost = 9
    monthly_income = total_subscribers * subscription_cost
    result = monthly_income
    return result

print(solution())