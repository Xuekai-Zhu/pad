def solution():
    """Two cups of flour are needed to make a dozen cookies. Carla is making 36 cookies today and 30 cookies tomorrow. How many cups of flour will Carla need to bake the cookies today and tomorrow?"""
    cookies_today = 36
    cookies_tomorrow = 30
    cookies_total = cookies_today + cookies_tomorrow
    flour_per_dozen = 2
    flour_total = (cookies_total / 12) * flour_per_dozen
    result = flour_total
    return result

print(solution())