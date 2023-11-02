def solution():
    """For every black & white cookie that Elsa makes, she has to make the batter, bake the cookies for 15 minutes and then allow to cool.  She then has to dip the cookies in white icing and allow the icing to harden for 30 minutes. Then she has to re-dip them in chocolate icing and allowed to harden for an additional 30 minutes.  If it takes her 2 hours to make the cookies from start to finish, how long does it take to make the dough and cool the cookies before she can start dipping them?"""
    # Define the time it takes to bake and cool a cookie
    COOKIE_TIME = 75 # 15 minutes to bake and 60 minutes to cool (30 + 30)

    # Calculate the time it takes to make one cookie
    ONE_COOKIE_TIME = COOKIE_TIME * 2 # multiplying by 2 for the two dips

    # Calculate the number of cookies Elsa can make in 2 hours
    NUM_COOKIES = int((2 * 60) / ONE_COOKIE_TIME)

    # Calculate the time it takes to make the dough and cool the cookies for 1 cookie
    DOUGH_COOL_TIME = COOKIE_TIME / 2 # half of the time it takes to make one cookie

    # Calculate the total time it takes to make the dough and cool the cookies for all the cookies
    TOTAL_DOUGH_COOL_TIME = NUM_COOKIES * DOUGH_COOL_TIME

    # Display the total time it takes to make the dough and cool the cookies
    result = TOTAL_DOUGH_COOL_TIME
    return result

print(solution())