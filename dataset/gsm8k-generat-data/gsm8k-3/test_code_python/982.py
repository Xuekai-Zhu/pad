def solution():
    """Frank bakes two trays of cookies per day, for 6 days. Frank eats one cookie each day to make sure they taste good. Ted comes over on the sixth day and eats 4 cookies. If each tray makes 12 cookies, how many cookies are left when Ted leaves?"""
    # Define the number of trays and cookies baked per day
    TRAYS_PER_DAY = 2
    COOKIES_PER_TRAY = 12

    # Define the number of days Frank bakes
    days_baked = 6

    # Calculate the total number of cookies baked by Frank
    total_cookies = TRAYS_PER_DAY * COOKIES_PER_TRAY * days_baked

    # Subtract the cookies Frank ate during the baking process
    total_cookies -= days_baked

    # Subtract the cookies Ted ate
    total_cookies -= 4

    # Display the number of cookies left
    result = total_cookies
    return result

print(solution())