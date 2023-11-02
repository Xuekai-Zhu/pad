def solution():
    # Calculate the total number of cookies made by Danny
    total_cookies = 4 * 12  # 4 dozen cookies

    # Calculate the total number of chips in all the cookies
    total_chips = total_cookies * 7  # each cookie has 7 chips

    # Calculate the number of chips left uneaten after the class eats half the cookies
    uneaten_chips = (total_chips / 2) % 7  # each cookie has 7 chips
    result = uneaten_chips
    return result

print(solution())