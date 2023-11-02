def solution():
    """Frank bakes two trays of cookies per day, for 6 days. Frank eats one cookie each day to make sure they taste good. Ted comes over on the sixth day and eats 4 cookies. If each tray makes 12 cookies, how many cookies are left when Ted leaves?"""
    trays_per_day = 2
    total_days = 6
    cookies_per_tray = 12
    total_cookies = trays_per_day * cookies_per_tray * total_days
    total_cookies -= total_days  # subtract Frank's testing cookies
    total_cookies -= 4  # subtract Ted's cookies
    result = total_cookies
    return result

print(solution())