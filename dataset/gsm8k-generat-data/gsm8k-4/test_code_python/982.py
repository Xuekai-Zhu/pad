def solution():
    """Frank bakes two trays of cookies per day, for 6 days. Frank eats one cookie each day to make sure they taste good. Ted comes over on the sixth day and eats 4 cookies. If each tray makes 12 cookies, how many cookies are left when Ted leaves?"""
    # Define the number of trays baked each day
    trays_baked_per_day = 2

    # Define the number of days baked
    days_baked = 6

    # Define the number of cookies in each tray
    cookies_per_tray = 12

    # Calculate the total number of cookies baked
    total_cookies = trays_baked_per_day * days_baked * cookies_per_tray

    # Calculate the number of cookies Frank ate
    cookies_frank_ate = days_baked + 1

    # Calculate the number of cookies Ted ate
    cookies_ted_ate = 4

    # Calculate the number of cookies left
    cookies_left = total_cookies - cookies_frank_ate - cookies_ted_ate

    # return the result
    result = cookies_left
    return result

print(solution())