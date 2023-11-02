def solution():
    
    payment_per_post = 0.25
    seconds_per_hour = 3600
    posts_per_hour = seconds_per_hour / 10
    earnings_per_hour = posts_per_hour * payment_per_post
    result = earnings_per_hour
    return result

print(solution())