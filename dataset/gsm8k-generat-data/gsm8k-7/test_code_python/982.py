def solution():
    trays_per_day = 2
    num_days = 6
    num_cookies_per_tray = 12
    frank_eats_per_day = 1
    ted_eats_on_sixth_day = 4

    # Calculate the total number of cookies baked by Frank
    total_cookies_baked = trays_per_day * num_cookies_per_tray * num_days

    # Calculate the number of cookies Frank eats during the 6-day period
    total_frank_eats = frank_eats_per_day * num_days

    # Calculate the number of cookies Ted and Frank eat together on the 6th day
    total_ted_and_frank_eats_on_sixth = ted_eats_on_sixth_day + frank_eats_per_day

    # Calculate the final number of cookies left
    cookies_left = total_cookies_baked - total_frank_eats - total_ted_and_frank_eats_on_sixth
    result = cookies_left
    return result

print(solution())