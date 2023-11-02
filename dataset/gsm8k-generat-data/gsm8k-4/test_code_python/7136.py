def solution():
    """Danny made chocolate cookies for his class and made sure each cookie had exactly 7 chips. He made 4 dozen in total. If the class eats half the cookies, how many chips are left uneaten?"""
    # Define the number of cookies baked
    cookies_baked = 4 * 12

    # Define the number of chips per cookie
    chips_per_cookie = 7

    # Calculate the total number of chips baked
    total_chips = cookies_baked * chips_per_cookie

    # Calculate the number of chips eaten by the class
    chips_eaten = (cookies_baked / 2) * chips_per_cookie

    # Calculate the number of chips left uneaten
    chips_left = total_chips - chips_eaten

    result = chips_left
    return result

print(solution())