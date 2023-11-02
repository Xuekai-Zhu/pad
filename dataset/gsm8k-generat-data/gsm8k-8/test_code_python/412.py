def solution():
    # Define the number of cookies given to Tim and Mike
    tim_cookies = 15
    mike_cookies = 23

    # Calculate the number of cookies given to Anna
    anna_cookies = 2 * tim_cookies

    # Calculate the total number of cookies given away
    given_cookies = tim_cookies + mike_cookies + anna_cookies

    # Calculate the number of cookies left in the fridge
    fridge_cookies = 256 - given_cookies

    result = fridge_cookies
    return result

print(solution())