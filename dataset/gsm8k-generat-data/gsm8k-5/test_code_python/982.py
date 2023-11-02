def solution():
    trays_per_day = 2  # Frank bakes two trays of cookies per day
    days = 6  # Frank bakes cookies for 6 days
    cookies_per_tray = 12  # Each tray makes 12 cookies
    total_cookies = trays_per_day * cookies_per_tray * days  # Calculate total number of cookies baked
    total_cookies -= (6 * 1)  # Subtract the cookies Frank ate for taste-testing
    total_cookies -= 4  # Subtract the cookies Ted ate
    result = total_cookies
    return result

print(solution())