def solution():
    """Maria has 19 cookies. She decided to give her friend 5 of them, and half of the rest to her family. From the rest, Maria decided to eat 2 cookies. How many cookies will she have left?"""
    # Define the initial number of cookies
    cookies = 19

    # Give 5 cookies to a friend
    cookies -= 5

    # Calculate the number of cookies remaining
    remaining_cookies = cookies

    # Give half of the remaining cookies to her family
    family_cookies = remaining_cookies / 2
    remaining_cookies -= family_cookies

    # Eat 2 cookies from the remaining
    remaining_cookies -= 2

    # Display the number of cookies Maria has left
    result = remaining_cookies
    return result

print(solution())