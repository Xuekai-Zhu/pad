def solution():
    
    total_cookies = 70
    cookies_left = 28
    cookies_taken = total_cookies - cookies_left
    cookies_per_day = cookies_taken / 7
    cookies_taken_in_four_days = cookies_per_day * 4
    result = cookies_taken_in_four_days
    return result

print(solution())