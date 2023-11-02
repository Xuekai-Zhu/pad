def solution():
    cookies_left_day2 = 8  # Jen had 8 cookies left on the third day
    cookies_remaining_day1 = (1/4) * cookies_left_day2  # Jen ate three-quarters of the bag on the first day, so there were 1/4 left
    cookies_in_bag = (2 * cookies_remaining_day1) + cookies_left_day2  # Jen ate half the remaining cookies on the second day

    result = cookies_in_bag
    return result

print(solution())