def solution():
    """For every black & white cookie that Elsa makes, she has to make the batter, bake the cookies for 15 minutes and then allow to cool. She then has to dip the cookies in white icing and allow the icing to harden for 30 minutes. Then she has to re-dip them in chocolate icing and allowed to harden for an additional 30 minutes. If it takes her 2 hours to make the cookies from start to finish, how long does it take to make the dough and cool the cookies before she can start dipping them?"""
    total_time = 2 * 60  # convert 2 hours to minutes
    baking_time = 15
    white_icing_time = 30
    chocolate_icing_time = 30
    total_cookie_time = baking_time + white_icing_time + chocolate_icing_time
    num_cookies = total_time // total_cookie_time
    dough_cooling_time = total_time - (num_cookies * total_cookie_time)
    result = dough_cooling_time
    return result

print(solution())