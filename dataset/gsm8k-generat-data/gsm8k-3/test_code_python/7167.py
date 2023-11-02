def solution():
    """Maria has 19 cookies. She decided to give her friend 5 of them, and half of the rest to her family. From the rest, Maria decided to eat 2 cookies. How many cookies will she have left?"""
    # Define the initial number of cookies
    initial_cookies = 19

    # Calculate the number of cookies left after giving some to her friend
    cookies_left = initial_cookies - 5

    # Calculate the number of cookies to give to her family
    family_cookies = cookies_left / 2

    # Calculate the number of cookies left after giving some to her family
    cookies_left = cookies_left - family_cookies

    # Calculate the number of cookies left after Maria eats 2
    cookies_left = cookies_left - 2

    # Display the number of cookies left
    result = cookies_left
    return result

print(solution())