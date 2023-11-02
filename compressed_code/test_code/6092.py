def solution():
    
    total_cookies = 256
    cookies_given_tim = 15
    cookies_given_mike = 23
    cookies_given_others = cookies_given_tim + cookies_given_mike
    cookies_remaining = total_cookies - cookies_given_others
    cookies_given_anna = cookies_given_tim * 2
    cookies_in_fridge = cookies_remaining - cookies_given_anna
    result = cookies_in_fridge
    
    return result

print(solution())