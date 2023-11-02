def solution():
    """Neil baked 20 cookies. He gave 2/5 of the cookies to his friend. How many cookies are left for Neil?"""
    # Define the initial number of cookies
    initial_cookies = 20

    # Calculate the number of cookies given to Neil's friend
    friend_cookies = initial_cookies * (2/5)

    # Calculate the number of cookies left for Neil
    neil_cookies = initial_cookies - friend_cookies

    # return the result
    result = neil_cookies
    return result

print(solution())