def solution():
    """Clementine, Jake, and Tory make cookies for the school bake sale. Clementine baked 72 cookies. Jake baked twice as many cookies as Clementine. Tory baked half as many cookies as Jake and Clementine combined. They sell their cookies for $2 each. If they sell all their cookies, how much money do they make?"""
    clementine_cookies = 72
    jake_cookies = clementine_cookies * 2
    tory_cookies = (clementine_cookies + jake_cookies) / 2
    total_cookies = clementine_cookies + jake_cookies + tory_cookies
    price_per_cookie = 2
    money_made = total_cookies * price_per_cookie
    result = money_made
    return result

print(solution())