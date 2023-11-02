def solution():
    """Danny made chocolate cookies for his class and made sure each cookie had exactly 7 chips. He made 4 dozen in total. If the class eats half the cookies, how many chips are left uneaten?"""
    cookies_in_dozen = 12
    total_cookies = 4 * cookies_in_dozen
    eaten_cookies = total_cookies / 2
    chips_per_cookie = 7
    total_chips = total_cookies * chips_per_cookie
    eaten_chips = eaten_cookies * chips_per_cookie
    chips_left = total_chips - eaten_chips
    result = chips_left
    return result

print(solution())