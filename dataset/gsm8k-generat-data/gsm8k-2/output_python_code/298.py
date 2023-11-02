def solution():
    """Basil gets 1/2 of a dog cookie in the morning and before bed. She gets 2 whole cookies during the day. Basil’s cookies are packaged with 45 cookies per box. How many boxes will she need to last her for 30 days?"""
    morning_and_evening_cookies_per_day = 1
    day_cookies_per_day = 2
    total_cookies_per_day = morning_and_evening_cookies_per_day + day_cookies_per_day
    cookies_per_box = 45
    total_cookies_per_30_days = total_cookies_per_day * 30
    total_half_cookies_per_30_days = morning_and_evening_cookies_per_day * 30
    total_whole_cookies_per_30_days = day_cookies_per_day * 30
    total_cookies = (total_half_cookies_per_30_days / 2) + total_whole_cookies_per_30_days
    total_boxes = total_cookies / cookies_per_box
    result = total_boxes
    return result

print(solution())