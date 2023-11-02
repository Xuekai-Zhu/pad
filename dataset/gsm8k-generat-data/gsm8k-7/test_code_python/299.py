def solution():
    morning_cookie = 1/2
    bedtime_cookie = 1/2
    daytime_cookie = 2
    total_cookies_per_day = morning_cookie + bedtime_cookie + daytime_cookie
    cookies_per_box = 45
    days = 30
    total_cookies_needed = total_cookies_per_day * days
    boxes_needed = total_cookies_needed / cookies_per_box
    result = boxes_needed
    return result

print(solution())