def solution():
    # Calculate the number of cookies in the bag to start
    cookies_left_after_first_day = (1/4) * Jen_cookies  # Jen ate three-quarters of the bag on the first day
    cookies_left_after_second_day = (1/2) * cookies_left_after_first_day  # Jen ate half of the remaining cookies on the second day
    cookies_in_the_bag_to_start = 8 / (1/2)  # Jen had 8 cookies left on the third day
    result = cookies_in_the_bag_to_start
    return result

print(solution())