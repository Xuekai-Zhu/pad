def solution():
    total_cookies = 200
    cookies_taken_by_wife = total_cookies * 0.3
    cookies_taken_by_daughter = total_cookies * 0.4
    cookies_left = total_cookies - cookies_taken_by_wife - cookies_taken_by_daughter
    cookies_eaten = cookies_left / 2
    cookies_not_eaten = cookies_left - cookies_eaten
    result = cookies_not_eaten
    return result

print(solution())