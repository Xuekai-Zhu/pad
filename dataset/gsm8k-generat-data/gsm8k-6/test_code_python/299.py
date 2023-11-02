def solution():
    # Calculate the number of cookies Basil gets per day
    cookies_per_day = (1/2) * 2 + 2  # Basil gets 1/2 of a cookie in the morning and before bed, and 2 whole cookies during the day

    # Calculate the total number of cookies needed for 30 days
    total_cookies = cookies_per_day * 30

    # Calculate the number of boxes needed
    boxes_needed = total_cookies / 45

    result = boxes_needed
    return result

print(solution())