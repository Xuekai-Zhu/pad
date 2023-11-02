def solution():
    total_cookies = 70
    cookies_left = 28
    days_passed = 7
    cookies_taken_per_day = (total_cookies - cookies_left) / days_passed
    cookies_taken_in_four_days = cookies_taken_per_day * 4
    result = cookies_taken_in_four_days
    return result

print(solution())