def solution():
    """Uncle Jude baked 256 cookies. He gave 15 cookies to Tim, 23 cookies to Mike, kept some in the fridge and gave the rest to Anna. How many cookies did he put in the fridge if he gave twice as many cookies as he gave Tim to Anna?"""
    # Define the number of cookies given to Tim and Mike
    TIM_COOKIES = 15
    MIKE_COOKIES = 23

    # Calculate the total number of cookies given away
    given_away = TIM_COOKIES + MIKE_COOKIES

    # Calculate the number of cookies given to Anna
    anna_cookies = given_away * 2

    # Calculate the number of cookies in the fridge
    fridge_cookies = 256 - given_away - anna_cookies

    # Display the number of cookies in the fridge
    result = fridge_cookies
    return result

print(solution())