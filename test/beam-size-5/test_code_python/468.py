def solution():
    
    total_cookies = 5
    extra_cookies = 2
    cookies_eaten = total_cookies / (1 + extra_cookies)
    carrot_sticks_eaten = cookies_eaten / 2
    result = carrot_sticks_eaten
    return result

print(solution())