def solution():
    cookies_per_dozen = 12  # There are 12 cookies in a dozen
    cookies_bought = 2 * cookies_per_dozen  # John bought 2 dozen cookies
    cookies_eaten = 3  # John ate 3 cookies

    # Calculate the number of cookies left
    cookies_left = cookies_bought - cookies_eaten
    result = cookies_left
    return result

print(solution())