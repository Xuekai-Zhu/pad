def solution():
    
    trays_per_day = 2
    total_days = 6
    cookies_per_tray = 12
    total_cookies = trays_per_day * cookies_per_tray * total_days
    total_cookies -= total_days  
    total_cookies -= 4  
    result = total_cookies
    return result

print(solution())