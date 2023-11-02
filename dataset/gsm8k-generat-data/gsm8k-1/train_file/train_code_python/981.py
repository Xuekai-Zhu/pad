def solution():
    """Frank bakes two trays of cookies per day, for 6 days. Frank eats one cookie each day to make sure they taste good. Ted comes over on the sixth day and eats 4 cookies. If each tray makes 12 cookies, how many cookies are left when Ted leaves?"""
    trays_per_day = 2
    days = 6
    cookies_per_tray = 12
    total_cookies = trays_per_day * cookies_per_tray * days
    frank_cookies = days  # Frank eats one cookie each day
    ted_cookies = 4
    cookies_left = total_cookies - frank_cookies - ted_cookies
    result = cookies_left
    return result

print(solution())