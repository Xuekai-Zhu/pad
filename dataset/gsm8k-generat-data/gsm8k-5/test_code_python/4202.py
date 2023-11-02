def solution():
    # Calculate the total time it takes to bake and dip the cookies
    total_cookie_time = 15 + 30 + 30  # 15 minutes to bake, 30 minutes for white icing, and 30 minutes for chocolate icing

    # Calculate the time it takes to make one cookie
    time_per_cookie = total_cookie_time / 1  # Elsa makes one cookie at a time

    # Calculate the number of cookies Elsa can make in 2 hours
    cookies_per_batch = 1  # Elsa makes one cookie at a time
    batch_time = 2 * 60  # Elsa has 2 hours to make cookies
    cookies_per_batch_time = batch_time // time_per_cookie
    total_cookies = cookies_per_batch_time * cookies_per_batch

    # Calculate the time it takes to make the dough and cool the cookies
    dough_cool_time = total_cookie_time * total_cookies  # Elsa has to make and cool the dough for each cookie
    result = dough_cool_time
    return result

print(solution())