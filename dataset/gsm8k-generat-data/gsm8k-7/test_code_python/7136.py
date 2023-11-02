def solution():
    chips_per_cookie = 7
    cookies_made = 4 * 12  # 4 dozen
    cookies_eaten = cookies_made / 2  # half eaten

    # Calculate the total number of chips in all cookies made
    total_chips = chips_per_cookie * cookies_made

    # Calculate the total number of chips in cookies eaten
    eaten_chips = chips_per_cookie * cookies_eaten

    # Calculate the number of chips left uneaten
    uneaten_chips = total_chips - eaten_chips
    result = uneaten_chips
    return result

print(solution())