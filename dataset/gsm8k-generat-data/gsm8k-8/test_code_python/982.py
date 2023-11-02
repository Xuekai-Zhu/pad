def solution():
    trays_per_day = 2
    days = 6
    cookies_per_tray = 12
    total_cookies = trays_per_day * days * cookies_per_tray
    total_cookies -= days # subtract Frank's daily cookie
    total_cookies -= 4 # subtract Ted's cookies
    result = total_cookies
    return result

print(solution())