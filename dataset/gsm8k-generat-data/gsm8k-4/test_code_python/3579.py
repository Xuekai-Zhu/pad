def solution():
    """Theo drinks 8 cups of water every day. Mason drinks 7 cups of water. Roxy drinks 9 cups of water every day. In one week, how many cups of water do the siblings drink together?"""
    # Define the daily water intake for each sibling
    theo_daily = 8
    mason_daily = 7
    roxy_daily = 9

    # Calculate the weekly water intake for each sibling
    theo_weekly = theo_daily * 7
    mason_weekly = mason_daily * 7
    roxy_weekly = roxy_daily * 7

    # Calculate the total weekly water intake for the siblings
    weekly_total = theo_weekly + mason_weekly + roxy_weekly

    # return the result
    result = weekly_total
    return result

print(solution())