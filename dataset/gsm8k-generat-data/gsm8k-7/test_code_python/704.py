def solution():
    starting_cookies = 20
    brother_cookies = 10
    mother_cookies = brother_cookies / 2
    sabrina_cookies = starting_cookies - brother_cookies - mother_cookies
    sister_cookies = sabrina_cookies * (2/3)
    cookies_left = starting_cookies - brother_cookies - mother_cookies - sister_cookies
    result = cookies_left
    return result

print(solution())