def solution():
    """Sabrina gave 10 cookies to her brother. Her mother gave Sabrina half the number of cookies she gave her brother. Then Sabrina gave two-thirds of her cookies to her sister. If Sabrina had 20 cookies at the start, how many cookies are left with her?"""
    # Define the number of cookies Sabrina started with
    cookies_start = 20

    # Calculate the number of cookies Sabrina had after giving 10 to her brother
    cookies_after_brother = cookies_start - 10

    # Calculate the number of cookies Sabrina's mother gave her
    mother_cookies = 10 / 2

    # Calculate the number of cookies Sabrina had after receiving cookies from her mother
    cookies_after_mother = cookies_after_brother + mother_cookies

    # Calculate the number of cookies Sabrina gave to her sister
    sister_cookies = cookies_after_mother * (2 / 3)

    # Calculate the number of cookies Sabrina has left
    cookies_left = cookies_after_mother - sister_cookies

    # Display the number of cookies left with Sabrina
    result = cookies_left
    return result

print(solution())