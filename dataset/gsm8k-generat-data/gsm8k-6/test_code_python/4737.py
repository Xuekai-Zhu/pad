def solution():
    # Find the number of black cookies Cristian initially had
    initial_white_cookies = 80
    black_cookies = initial_white_cookies + 50

    # Find the number of black cookies Cristian has left after eating half of them
    remaining_black_cookies = black_cookies / 2

    # Find the number of white cookies Cristian has left after eating 3/4 of them
    remaining_white_cookies = initial_white_cookies / 4

    # Find the total number of cookies in the cookie jar after Cristian has eaten some of them
    total_cookies = remaining_black_cookies + remaining_white_cookies

    result = total_cookies
    return result

print(solution())