def solution():
    cookies_per_tray = 12
    trays_baked_per_day = 2
    days_baked = 6
    cookies_eaten = 1
    cookies_given_away = 4
    total_cookies = cookies_per_tray * trays_baked_per_day * days_baked
    cookies_left = total_cookies - cookies_eaten - cookies_given_away
    result = cookies_left
    return result

print(solution())