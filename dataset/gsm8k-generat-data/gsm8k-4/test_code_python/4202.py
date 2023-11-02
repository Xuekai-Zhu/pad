def solution():
    """ For every black & white cookie that Elsa makes, she has to make the batter, bake the cookies for 15 minutes
    and then allow to cool.  She then has to dip the cookies in white icing and allow the icing to harden for 30 minutes. Then
     she has to re-dip them in chocolate icing and allowed to harden for an additional 30 minutes.  If it takes her 2 hours to make
    the cookies from start to finish, how long does it take to make the dough and cool the cookies before she can start dipping them?
    """
    # Define the time it takes to bake and cool the cookies
    bake_cool_time = 15 + 30 + 30  # minutes

    # Define the total time it takes to make a single cookie
    single_cookie_time = bake_cool_time * 2

    # Define the total number of cookies Elsa can make in 2 hours
    total_cookies = (2 * 60) // single_cookie_time

    # Calculate the total time it takes to make the batter and cool the cookies for the total number of cookies
    dough_cool_time = bake_cool_time * total_cookies

    # Convert the time to hours and minutes
    hours = dough_cool_time // 60
    minutes = dough_cool_time % 60

    # Return the result as a string in the format of "x hours y minutes"
    result = "{} hours {} minutes".format(int(hours), int(minutes))
    return result

print(solution())