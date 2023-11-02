def solution():
    """Uncle Jude baked 256 cookies. He gave 15 cookies to Tim, 23 cookies to Mike, kept some in the fridge and gave the rest to Anna. How many cookies did he put in the fridge if he gave twice as many cookies as he gave Tim to Anna?"""
    # Define the number of cookies baked and the number given to Tim and Mike
    total_cookies = 256
    tim_cookies = 15
    mike_cookies = 23

    # Calculate the total number of cookies given away
    given_cookies = tim_cookies + mike_cookies

    # Calculate the number of cookies given to Anna
    anna_cookies = (given_cookies * 2)

    # Calculate the number of cookies put in the fridge
    fridge_cookies = total_cookies - given_cookies - anna_cookies

    result = fridge_cookies
    return result

print(solution())