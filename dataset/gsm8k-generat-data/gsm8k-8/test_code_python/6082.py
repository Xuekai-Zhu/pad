def solution():
    # Define Glenn's number of cookies
    glenn_cookies = 24

    # Calculate Kenny's number of cookies (half of Chris's)
    kenny_cookies = 2 * glenn_cookies

    # Calculate Chris's number of cookies
    chris_cookies = kenny_cookies / 2

    # Calculate the total number of cookies
    total_cookies = glenn_cookies + kenny_cookies + chris_cookies
    result = total_cookies
    return result

print(solution())