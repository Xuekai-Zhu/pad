def solution():
    """Janet is getting paid to moderate social media posts. She gets paid 25 cents per post she checks. If it takes her 10 seconds to check a post, how much does she earn per hour?"""
    pay_per_post = 0.25
    time_per_post = 10 #seconds
    posts_per_hour = 3600 / time_per_post
    hourly_pay = pay_per_post * posts_per_hour
    result = hourly_pay
    return result

print(solution())