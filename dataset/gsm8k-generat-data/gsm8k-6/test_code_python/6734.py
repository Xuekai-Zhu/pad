def solution():
    # Calculate the total number of cookies sold by Katrina
    cookies_sold = (3*12) + 57 + 16  # 3 dozen cookies in the morning, 57 cookies during lunch, and 16 more in the afternoon
    cookies_left = 120 - cookies_sold  # calculate the remaining cookies to take home
    result = cookies_left
    return result

print(solution())