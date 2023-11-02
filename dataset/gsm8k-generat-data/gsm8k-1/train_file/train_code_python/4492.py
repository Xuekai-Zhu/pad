def solution():
    """Janet is getting paid to moderate social media posts. She gets paid 25 cents per post she checks. If it takes her 10 seconds to check a post, how much does she earn per hour?"""
    payment_per_post = 0.25
    seconds_per_hour = 3600
    posts_per_hour = seconds_per_hour / 10
    earnings_per_hour = posts_per_hour * payment_per_post
    result = earnings_per_hour
    return result

print(solution())