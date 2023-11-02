def solution():
    
    pay_per_post = 0.25
    time_per_post = 10 
    posts_per_hour = 3600 / time_per_post
    hourly_pay = pay_per_post * posts_per_hour
    result = hourly_pay
    return result

print(solution())