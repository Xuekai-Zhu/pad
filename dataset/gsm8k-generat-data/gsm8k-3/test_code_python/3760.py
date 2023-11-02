def solution():
    """Clementine, Jake, and Tory make cookies for the school bake sale. Clementine baked 72 cookies. Jake baked twice as many cookies as Clementine. Tory baked half as many cookies as Jake and Clementine combined. They sell their cookies for $2 each. If they sell all their cookies, how much money do they make?"""
    # Define the number of cookies baked by each person
    clementine_cookies = 72
    jake_cookies = 2 * clementine_cookies
    tory_cookies = (jake_cookies + clementine_cookies) / 2

    # Calculate the total number of cookies
    total_cookies = clementine_cookies + jake_cookies + tory_cookies

    # Calculate the total amount of money made
    total_money = total_cookies * 2

    # Display the total amount of money made
    result = total_money
    return result

print(solution())