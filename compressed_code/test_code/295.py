def solution():
    
    total_cookies = 256
    tim_cookies = 15
    mike_cookies = 23
    anna_cookies = total_cookies - tim_cookies - mike_cookies
    tim_to_anna_cookies = 2 * tim_cookies
    cookies_in_fridge = anna_cookies - tim_to_anna_cookies
    result = cookies_in_fridge
    return result

print(solution())