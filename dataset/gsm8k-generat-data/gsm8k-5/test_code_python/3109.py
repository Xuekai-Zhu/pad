def solution():
    initial_cookies = 0  # Number of cookies in the jar initially
    cookies_eaten = 3 + 2  # Lou Senior ate 3 cookies one day, then 2 the next day
    cookies_returned = 2  # Lou Senior ate 3 cookies but returned 2 the next day
    cookies_hidden = 7  # Louie Junior took 7 cookies and hid them in his bedroom

    # Calculate the number of cookies remaining in the jar
    remaining_cookies = initial_cookies + cookies_eaten - cookies_returned - cookies_hidden
    result = remaining_cookies
    return result

print(solution())