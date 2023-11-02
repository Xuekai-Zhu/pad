def solution():
    morning_cookie = 0.5  # Basil gets 1/2 of a cookie in the morning
    evening_cookie = 0.5  # Basil gets 1/2 of a cookie before bed
    day_cookie = 2  # Basil gets 2 whole cookies during the day
    cookies_per_box = 45  # There are 45 cookies per box
    days = 30  # Basil wants to know how many boxes she will need for 30 days

    # Calculate the total number of cookies Basil will need for 30 days
    total_cookies = (morning_cookie + evening_cookie) * 2 + day_cookie * 30
    # Calculate the total number of boxes Basil will need for 30 days
    total_boxes = total_cookies / cookies_per_box
    result = total_boxes
    return result

print(solution())