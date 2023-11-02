def solution():
    """Theo, Mason, and Roxy are siblings. Theo drinks 8 cups of water every day. Mason drinks 7 cups of water. Roxy drinks 9 cups of water every day. In one week, how many cups of water do the siblings drink together?"""
    theo_daily = 8
    mason_daily = 7
    roxy_daily = 9
    days_in_week = 7
    total_water = (theo_daily + mason_daily + roxy_daily) * days_in_week
    result = total_water
    return result

print(solution())