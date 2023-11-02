def solution():
    cookies_made = 4*12  # Danny made 4 dozen chocolate cookies
    chips_per_cookie = 7  # Each cookie had exactly 7 chips
    total_chips = cookies_made * chips_per_cookie  # Total number of chips in all the cookies
    eaten_cookies = cookies_made / 2  # Half of the cookies were eaten by the class
    eaten_chips = eaten_cookies * chips_per_cookie  # Total number of chips eaten by the class
    uneaten_chips = total_chips - eaten_chips  # Number of chips left uneaten
    result = uneaten_chips
    return result

print(solution())