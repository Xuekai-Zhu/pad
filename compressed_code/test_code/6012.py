def solution():
    
    morning_cookie = 0.5
    evening_cookie = 0.5
    day_cookie = 2
    cookies_per_day = morning_cookie + evening_cookie + day_cookie
    cookies_required = cookies_per_day * 30
    cookies_per_box = 45
    boxes_required = cookies_required / cookies_per_box
    result = boxes_required
    return result

print(solution())