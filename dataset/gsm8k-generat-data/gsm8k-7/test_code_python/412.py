def solution():
    total_cookies = 256
    tim_cookies = 15
    mike_cookies = 23

    # Calculate the total number of cookies given away
    given_cookies = tim_cookies + mike_cookies

    # Calculate the number of cookies given to Anna
    anna_cookies = given_cookies * 2

    # Calculate the number of cookies in the fridge
    fridge_cookies = total_cookies - given_cookies - anna_cookies
    result = fridge_cookies
    return result

print(solution())